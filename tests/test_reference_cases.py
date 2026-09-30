from __future__ import annotations

import json
import unittest
from pathlib import Path

from caap_benchmark.adapters import MockAdapter
from caap_benchmark.events import TELEMETRY_KEY_BY_EVENT
from caap_benchmark.models import ResultState
from caap_benchmark.oracles import matched_oracles
from caap_benchmark.runner import BenchmarkRunner

ROOT = Path(__file__).resolve().parents[1]
CASES = sorted((ROOT / "benchmarks/executable").rglob("*.json"))


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class ReferenceCaseTests(unittest.TestCase):
    """Every executable reference case must exercise its own mechanism, not a shared template."""

    def test_twenty_five_cases_each_with_a_scenario(self) -> None:
        self.assertEqual(len(CASES), 25)
        for path in CASES:
            case = _load(path)
            self.assertIn("mock_scenario", case, path.name)
            self.assertTrue(case["enabled"], path.name)

    def test_secure_trace_passes_on_mechanism_evidence(self) -> None:
        for path in CASES:
            case = _load(path)
            result = BenchmarkRunner(MockAdapter()).run(case)
            self.assertEqual(result.state, ResultState.PASS, f"{path.name}: {result.error}")
            self.assertEqual(result.attack_oracles_matched, [], path.name)
            expected = [oracle["id"] for oracle in case["secure_behavior_oracles"]]
            self.assertEqual(result.secure_oracles_matched, expected, path.name)
            self.assertEqual(result.missing_telemetry, [], path.name)

    def test_vulnerable_trace_fails_on_mechanism_oracle_first(self) -> None:
        for path in CASES:
            case = _load(path)
            result = BenchmarkRunner(MockAdapter(vulnerable=True)).run(case)
            self.assertEqual(result.state, ResultState.FAIL, path.name)
            mechanism_oracle = case["success_oracles"][0]["id"]
            self.assertNotEqual(mechanism_oracle, "sentinel-reached", path.name)
            self.assertEqual(
                result.attack_oracles_matched, [mechanism_oracle, "sentinel-reached"], path.name
            )

    def test_mechanism_oracle_cannot_fire_from_the_benign_objective_alone(self) -> None:
        for path in CASES:
            case = _load(path)
            response = MockAdapter().execute(case)
            self.assertEqual(matched_oracles(case["success_oracles"], response), [], path.name)

    def test_fixtures_and_oracles_are_distinct_across_cases(self) -> None:
        fixtures = {_load(path)["attack_fixture"]["content"] for path in CASES}
        oracles = {json.dumps(_load(path)["success_oracles"][0], sort_keys=True) for path in CASES}
        self.assertEqual(len(fixtures), 25)
        self.assertEqual(len(oracles), 25)

    def test_every_trace_event_has_a_telemetry_key(self) -> None:
        for path in CASES:
            case = _load(path)
            for mode in ("safe", "vulnerable"):
                for event in case["mock_scenario"][mode]["events"]:
                    self.assertIn(event["type"], TELEMETRY_KEY_BY_EVENT, f"{path.name}:{mode}")

    def test_sentinel_only_appears_in_the_vulnerable_trace(self) -> None:
        for path in CASES:
            case = _load(path)
            sentinel = case["safe_sentinel"]
            safe_events = json.dumps(case["mock_scenario"]["safe"]["events"])
            for event in case["mock_scenario"]["safe"]["events"]:
                self.assertNotEqual(event["type"], "sentinel_reached", path.name)
            self.assertNotIn("sentinel_reached", safe_events, path.name)
            self.assertIn(sentinel, case["attack_fixture"]["content"], path.name)


if __name__ == "__main__":
    unittest.main()
