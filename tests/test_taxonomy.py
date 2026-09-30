from __future__ import annotations

import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Normative baseline scores from CAAP v1.0.0-draft.1. These MUST NOT change (docs/STANDARD.md).
V1_BASELINE_SCORES = {
    "CAAP-CE-01": 9.4, "CAAP-CE-05": 9.4, "CAAP-CF-01": 9.2, "CAAP-EA-03": 9.0,
    "CAAP-GH-01": 6.8, "CAAP-GH-02": 8.6, "CAAP-GH-03": 7.1, "CAAP-GH-05": 7.8,
    "CAAP-HT-04": 7.8, "CAAP-IA-01": 8.7, "CAAP-IA-03": 7.6, "CAAP-IP-01": 8.1,
    "CAAP-IP-02": 8.7, "CAAP-IP-05": 7.7, "CAAP-MP-01": 8.6, "CAAP-MP-02": 8.7,
    "CAAP-MP-04": 8.6, "CAAP-RA-05": 9.2, "CAAP-SC-01": 9.1, "CAAP-SC-02": 9.3,
    "CAAP-SC-04": 9.0, "CAAP-TM-01": 8.6, "CAAP-TM-03": 7.4, "CAAP-TM-05": 9.0,
    "CAAP-TM-06": 7.6,
}
AXES = ("impact", "exploitability", "privilege", "autonomy", "persistence", "propagation")


def _derived(vector: dict) -> float:
    weights = (2, 2, 1, 1, 1, 1)
    return round(10 * sum(w * vector[a] for w, a in zip(weights, AXES, strict=True)) / 40, 1)


class TaxonomyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = json.loads((ROOT / "data/taxonomy/caap-200.json").read_text())

    def test_exactly_200_unique_patterns(self) -> None:
        patterns = self.registry["patterns"]
        self.assertEqual(len(patterns), 200)
        self.assertEqual(len({pattern["id"] for pattern in patterns}), 200)

    def test_expected_maturity_distribution(self) -> None:
        maturity = Counter(pattern["maturity"] for pattern in self.registry["patterns"])
        self.assertEqual(maturity, Counter(reference=25, candidate=40, catalog=135))

    def test_every_relationship_resolves(self) -> None:
        ids = {pattern["id"] for pattern in self.registry["patterns"]}
        for pattern in self.registry["patterns"]:
            for related in pattern["relationships"].values():
                self.assertFalse(set(related) - ids, pattern["id"])

    def test_v1_reference_scores_are_preserved(self) -> None:
        by_id = {pattern["id"]: pattern for pattern in self.registry["patterns"]}
        for pattern_id, score in V1_BASELINE_SCORES.items():
            severity = by_id[pattern_id]["severity"]
            self.assertEqual(severity["baseline_score"], score, pattern_id)
            self.assertEqual(severity["score_source"], "caap-v1.0-baseline", pattern_id)
            self.assertLessEqual(abs(score - _derived(severity["vector"])), 0.5, pattern_id)

    def test_non_reference_scores_derive_from_their_vectors(self) -> None:
        for pattern in self.registry["patterns"]:
            if pattern["id"] in V1_BASELINE_SCORES:
                continue
            severity = pattern["severity"]
            self.assertEqual(severity["score_source"], "vector-derived", pattern["id"])
            derived = _derived(severity["vector"])
            self.assertEqual(severity["baseline_score"], derived, pattern["id"])

    def test_severity_vectors_are_specific_and_in_range(self) -> None:
        vectors = set()
        for pattern in self.registry["patterns"]:
            vector = pattern["severity"]["vector"]
            self.assertEqual(set(vector), set(AXES), pattern["id"])
            self.assertTrue(all(1 <= vector[axis] <= 5 for axis in AXES), pattern["id"])
            vectors.add(tuple(vector[axis] for axis in AXES))
        # Previously every one of the 200 records shared a single vector.
        self.assertGreater(len(vectors), 50)

    def test_definitions_are_specific_and_unique(self) -> None:
        definitions = [pattern["definition"] for pattern in self.registry["patterns"]]
        self.assertEqual(len(set(definitions)), 200)
        for pattern in self.registry["patterns"]:
            definition = pattern["definition"]
            self.assertFalse(definition.startswith("Tests whether"), pattern["id"])
            self.assertGreaterEqual(len(definition), 80, pattern["id"])
            self.assertTrue(definition.endswith("."), pattern["id"])

    def test_generated_yaml_matches_canonical_json(self) -> None:
        try:
            import yaml
        except ImportError:
            self.skipTest("PyYAML is not installed")
        parsed = yaml.safe_load((ROOT / "data/taxonomy/caap-200.yaml").read_text(encoding="utf-8"))
        self.assertEqual(parsed, self.registry)


class YamlEmitterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "generate_catalog", ROOT / "scripts" / "generate_catalog.py"
        )
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        cls.dump_yaml = staticmethod(module.dump_yaml)

    def test_empty_containers_round_trip(self) -> None:
        try:
            import yaml
        except ImportError:
            self.skipTest("PyYAML is not installed")
        value = {
            "empty_list": [],
            "empty_dict": {},
            "items": [{"first": [], "second": {}}, [], {}, "text"],
            "nested": {"inner": {"deep": []}},
        }
        text = "\n".join(self.dump_yaml(value)) + "\n"
        self.assertEqual(yaml.safe_load(text), value)


if __name__ == "__main__":
    unittest.main()
