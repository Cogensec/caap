from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from caap_benchmark.adapters import MockAdapter
from caap_benchmark.adapters.http import _normalize
from caap_benchmark.loaders import structural_test_case_errors, validate_test_case
from caap_benchmark.models import ResultState
from caap_benchmark.reports import write_json
from caap_benchmark.runner import BenchmarkRunner
from caap_benchmark.schemas import (
    SCHEMA_NAMES,
    jsonschema_available,
    load_schema,
    schema_errors,
)
from caap_benchmark.scoring import score

ROOT = Path(__file__).resolve().parents[1]
CASE_PATH = ROOT / "benchmarks/executable/gh/CAAP-GH-01.json"


def _case() -> dict:
    return json.loads(CASE_PATH.read_text(encoding="utf-8"))


class BundledSchemaTests(unittest.TestCase):
    def test_bundled_schemas_match_canonical_files(self) -> None:
        for name in SCHEMA_NAMES:
            canonical = json.loads((ROOT / "schemas" / f"{name}.schema.json").read_text())
            self.assertEqual(load_schema(name), canonical, name)

    def test_unknown_schema_name_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            load_schema("nope")


class StructuralFallbackTests(unittest.TestCase):
    """The dependency-free check must track the schema's required fields."""

    def test_valid_case_has_no_errors(self) -> None:
        self.assertEqual(structural_test_case_errors(_case()), [])

    def test_every_schema_required_field_is_enforced(self) -> None:
        for field in load_schema("test-case")["required"]:
            case = _case()
            del case[field]
            errors = structural_test_case_errors(case)
            self.assertTrue(any(field in error for error in errors), field)

    def test_false_safety_declaration_is_rejected(self) -> None:
        case = _case()
        case["safety"]["no_persistence"] = False
        self.assertIn("safety.no_persistence must be true", structural_test_case_errors(case))


class ValidateTestCaseTests(unittest.TestCase):
    def test_all_cases_are_valid(self) -> None:
        for path in sorted((ROOT / "benchmarks").rglob("*.json")):
            self.assertEqual(validate_test_case(json.loads(path.read_text())), [], path.name)

    def test_missing_schema_only_field_is_reported(self) -> None:
        # pattern_version, target_profile, and expected_secure_behavior were required by the
        # schema but not by the previous hand-rolled check.
        for field in ("pattern_version", "target_profile", "expected_secure_behavior"):
            case = _case()
            del case[field]
            errors = validate_test_case(case)
            self.assertTrue(any(field in error for error in errors), (field, errors))


@unittest.skipUnless(jsonschema_available(), "jsonschema is not installed")
class FullSchemaTests(unittest.TestCase):
    def test_registry_validates(self) -> None:
        registry = json.loads((ROOT / "data/taxonomy/caap-200.json").read_text())
        self.assertEqual(schema_errors("taxonomy", registry), [])

    def test_schema_catches_constraints_the_fallback_does_not(self) -> None:
        case = _case()
        case["severity"]["baseline_score"] = 11
        errors = validate_test_case(case)
        self.assertTrue(any("severity/baseline_score" in error for error in errors), errors)

    def test_written_report_validates(self) -> None:
        result = BenchmarkRunner(MockAdapter()).run(_case())
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "caap-report.json"
            write_json(path, [result], score([result]))
            report = json.loads(path.read_text())
        self.assertEqual(schema_errors("report", report), [])

    def test_mock_adapter_response_validates(self) -> None:
        response = MockAdapter().execute(_case())
        payload = {
            "events": [{"type": event.type, "data": event.data} for event in response.events],
            "response": response.response,
            "telemetry": response.telemetry,
            "applicable": response.applicable,
            "error": response.error,
        }
        self.assertEqual(schema_errors("adapter-response", payload), [])


class AdapterPayloadTests(unittest.TestCase):
    def test_malformed_payloads_become_test_errors(self) -> None:
        for payload in (
            "not an object",
            {"events": "nope", "telemetry": {}},
            {"events": [{"data": {}}], "telemetry": {}},
            {"events": [{"type": "x", "data": "bad"}], "telemetry": {}},
            {"events": [], "telemetry": []},
            {"events": []},
        ):
            normalized = _normalize(payload)
            self.assertIsNotNone(normalized.error, payload)
            self.assertIn("invalid adapter response", normalized.error or "")
            result = BenchmarkRunner(_Static(normalized)).run(_case())
            self.assertEqual(result.state, ResultState.TEST_ERROR, payload)

    def test_well_formed_payload_is_normalized(self) -> None:
        normalized = _normalize({"events": [{"type": "x"}], "telemetry": {}, "response": "ok"})
        self.assertIsNone(normalized.error)
        self.assertEqual(normalized.events[0].type, "x")
        self.assertEqual(normalized.response, "ok")


class _Static:
    name = "static"

    def __init__(self, response) -> None:
        self._response = response

    def execute(self, test_case):
        return self._response


if __name__ == "__main__":
    unittest.main()
