from __future__ import annotations

import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


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
