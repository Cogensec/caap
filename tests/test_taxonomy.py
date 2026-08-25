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


if __name__ == "__main__":
    unittest.main()
