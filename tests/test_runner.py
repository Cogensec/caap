from __future__ import annotations

import json
import unittest
from pathlib import Path

from caap_benchmark.adapters import MockAdapter
from caap_benchmark.models import ResultState
from caap_benchmark.runner import BenchmarkRunner
from caap_benchmark.scoring import score

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "benchmarks/executable/gh/CAAP-GH-01.json"


class RunnerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.case = json.loads(CASE.read_text())

    def test_safe_mock_passes(self) -> None:
        result = BenchmarkRunner(MockAdapter()).run(self.case)
        self.assertEqual(result.state, ResultState.PASS)
        self.assertEqual(result.attack_oracles_matched, [])
        self.assertIn("policy-denied", result.secure_oracles_matched)
        self.assertRegex(result.evidence["sha256"], r"^[a-f0-9]{64}$")

    def test_vulnerable_mock_fails(self) -> None:
        result = BenchmarkRunner(MockAdapter(vulnerable=True)).run(self.case)
        self.assertEqual(result.state, ResultState.FAIL)
        self.assertIn("sentinel-reached", result.attack_oracles_matched)

    def test_missing_capability_is_not_applicable(self) -> None:
        self.case["mock_target"] = {"capabilities": []}
        result = BenchmarkRunner(MockAdapter()).run(self.case)
        self.assertEqual(result.state, ResultState.NOT_APPLICABLE)

    def test_score_excludes_non_decisive_results(self) -> None:
        passed = BenchmarkRunner(MockAdapter()).run(self.case)
        failed = BenchmarkRunner(MockAdapter(vulnerable=True)).run(self.case)
        card = score([passed, failed])
        self.assertEqual(card.security_score, 50.0)
        self.assertEqual(card.coverage_percent, 100.0)


if __name__ == "__main__":
    unittest.main()

