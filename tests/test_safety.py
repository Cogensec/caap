from __future__ import annotations

import unittest

from caap_benchmark.safety import MockTool, MockToolRegistry, SafetyViolation, SyntheticSink


class SafetyTests(unittest.TestCase):
    def test_sink_accepts_only_sentinel(self) -> None:
        sink = SyntheticSink()
        sink.record("CAAP_GH_01_SENTINEL")
        self.assertEqual(sink.records, ["CAAP_GH_01_SENTINEL"])
        with self.assertRaises(SafetyViolation):
            sink.record("not-a-caap-sentinel")

    def test_registry_denies_unknown_tool(self) -> None:
        registry = MockToolRegistry()
        registry.register(MockTool("echo", lambda value: value))
        self.assertEqual(registry.invoke("echo", {"synthetic": True}), {"synthetic": True})
        with self.assertRaises(SafetyViolation):
            registry.invoke("network", {})


if __name__ == "__main__":
    unittest.main()

