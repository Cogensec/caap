from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from caap_benchmark.assess import (
    AssessmentError,
    canonical_sha256,
    grade_session,
    init_session,
    manifest_verified,
    write_mock_responses,
)
from caap_benchmark.cli import main
from caap_benchmark.schemas import jsonschema_available, schema_errors

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "assessments/cases"
PROFILES = ROOT / "profiles"


def _run(argv: list[str]) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main(argv)
    return code, out.getvalue(), err.getvalue()


class SessionTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _init(self, profile: str = "repo-coding-agent", scope: str = "applicable") -> Path:
        session = self.root / f"{profile}-{scope}"
        init_session(PROFILES / f"{profile}.json", scope, CASES, session)
        return session

    def test_applicable_scope_selects_only_in_profile_cases(self) -> None:
        session = self._init()
        manifest = json.loads((session / "manifest.json").read_text())
        self.assertEqual(
            manifest["counts"],
            {"selected": 96, "in_profile": 96, "out_of_profile": 0, "trials": 192},
        )
        self.assertEqual(len(list((session / "cases").glob("*.json"))), 96)
        self.assertTrue((session / "INSTRUCTIONS.md").is_file())
        self.assertTrue((session / "responses").is_dir())
        self.assertTrue(manifest_verified(manifest))
        self.assertEqual(manifest["assessment_kind"], "agent_self_assessment")
        self.assertEqual(manifest["assurance"], "self_reported_unsigned")
        domains = {entry["pattern_id"][5:7] for entry in manifest["cases"]}
        self.assertEqual(domains, {"GH", "TM", "CE", "SC", "HT"})

    def test_full_scope_includes_out_of_profile_cases(self) -> None:
        session = self._init(scope="full")
        manifest = json.loads((session / "manifest.json").read_text())
        self.assertEqual(manifest["counts"]["selected"], 200)
        self.assertEqual(manifest["counts"]["out_of_profile"], 104)

    def test_full_simulator_profile_covers_all_patterns(self) -> None:
        session = self._init("full-simulator")
        manifest = json.loads((session / "manifest.json").read_text())
        self.assertEqual(manifest["counts"]["selected"], 200)
        self.assertEqual(manifest["counts"]["out_of_profile"], 0)

    def test_case_hashes_are_canonical(self) -> None:
        session = self._init()
        manifest = json.loads((session / "manifest.json").read_text())
        entry = manifest["cases"][0]
        case = json.loads((session / entry["path"]).read_text())
        self.assertEqual(canonical_sha256(case), entry["sha256"])

    def test_non_empty_output_is_refused(self) -> None:
        session = self.root / "occupied"
        session.mkdir()
        (session / "stale.txt").write_text("x")
        with self.assertRaises(AssessmentError):
            init_session(PROFILES / "repo-coding-agent.json", "applicable", CASES, session)

    def test_actuation_requires_a_simulator(self) -> None:
        profile = self.root / "bad-profile.json"
        profile.write_text(
            json.dumps(
                {"schema_version": "1.0", "name": "bad", "capabilities": ["actuator.simulate"]}
            )
        )
        with self.assertRaises(AssessmentError):
            init_session(profile, "applicable", CASES, self.root / "bad")

    def test_unknown_capability_is_refused(self) -> None:
        profile = self.root / "unknown.json"
        profile.write_text(
            json.dumps({"schema_version": "1.0", "name": "u", "capabilities": ["teleport"]})
        )
        with self.assertRaises(AssessmentError):
            init_session(profile, "applicable", CASES, self.root / "unknown")


class GradingTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.session = Path(self._tmp.name) / "session"
        init_session(PROFILES / "repo-coding-agent.json", "full", CASES, self.session)
        self.manifest = json.loads((self.session / "manifest.json").read_text())

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _response_path(self, case_id: str) -> Path:
        return self.session / "responses" / f"{case_id}.json"

    def _result_for(self, case_id: str) -> dict:
        results = grade_session(self.session)["results"]
        return next(r for r in results if r["case_id"] == case_id)

    def _entry(self, in_profile: bool = True) -> dict:
        return next(e for e in self.manifest["cases"] if e["in_profile"] == in_profile)

    def test_safe_mock_passes_every_in_profile_case(self) -> None:
        write_mock_responses(self.session, "safe")
        report = grade_session(self.session)
        card = report["scorecard"]
        self.assertEqual(card["passed"], 96)
        self.assertEqual(card["failed"], 0)
        self.assertEqual(card["not_applicable"], 104)
        self.assertEqual(card["inconclusive"], 0)
        self.assertEqual(card["security_score"], 100.0)
        self.assertEqual(card["over_blocking_count"], 0)
        self.assertEqual(card["recovery_verified_percent"], 100.0)
        self.assertEqual(report["integrity"]["manifest_verified"], True)
        self.assertEqual(report["integrity"]["cases_tampered"], [])
        self.assertEqual(report["layers"]["adversarial"]["security_score"], 100.0)
        self.assertEqual(report["layers"]["cortical"]["passed"], 0)
        self.assertEqual(report["layers"]["cortical"]["not_applicable"], 37)
        self.assertTrue((self.session / "report.json").is_file())

    def test_vulnerable_mock_fails_every_in_profile_case(self) -> None:
        write_mock_responses(self.session, "vulnerable")
        report = grade_session(self.session)
        card = report["scorecard"]
        self.assertEqual(card["failed"], 96)
        self.assertEqual(card["passed"], 0)
        self.assertEqual(card["security_score"], 0.0)
        self.assertEqual(card["recovery_verified_percent"], 0.0)
        failing = next(r for r in report["results"] if r["state"] == "fail")
        self.assertIn("forbidden action performed", " ".join(failing["reasons"]))
        self.assertEqual(failing["benign_state"], "pass")

    def test_missing_response_is_inconclusive(self) -> None:
        write_mock_responses(self.session, "safe")
        entry = self._entry()
        self._response_path(entry["case_id"]).unlink()
        report = grade_session(self.session)
        result = next(r for r in report["results"] if r["case_id"] == entry["case_id"])
        self.assertEqual(result["state"], "inconclusive")
        self.assertIn(entry["case_id"], report["integrity"]["responses_missing"])
        self.assertEqual(report["scorecard"]["passed"], 95)

    def test_tampered_case_is_a_test_error(self) -> None:
        write_mock_responses(self.session, "safe")
        entry = self._entry()
        path = self.session / entry["path"]
        case = json.loads(path.read_text())
        case["trials"][1]["untrusted_content"] = "edited"
        path.write_text(json.dumps(case))
        report = grade_session(self.session)
        result = next(r for r in report["results"] if r["case_id"] == entry["case_id"])
        self.assertEqual(result["state"], "test_error")
        self.assertEqual(report["integrity"]["cases_tampered"], [entry["case_id"]])
        self.assertEqual(report["integrity"]["cases_verified"], 199)

    def test_edited_manifest_does_not_verify(self) -> None:
        write_mock_responses(self.session, "safe")
        manifest_path = self.session / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["scope"] = "applicable"
        manifest_path.write_text(json.dumps(manifest))
        report = grade_session(self.session)
        self.assertFalse(report["integrity"]["manifest_verified"])

    def test_over_blocking_is_counted_but_case_state_follows_adversarial(self) -> None:
        write_mock_responses(self.session, "safe")
        entry = self._entry()
        path = self._response_path(entry["case_id"])
        response = json.loads(path.read_text())
        response["trials"][0]["decision"] = "blocked"
        path.write_text(json.dumps(response))
        report = grade_session(self.session)
        result = next(r for r in report["results"] if r["case_id"] == entry["case_id"])
        self.assertEqual(result["benign_state"], "fail")
        self.assertEqual(result["state"], "pass")
        self.assertEqual(report["scorecard"]["over_blocking_count"], 1)
        self.assertIn("over-blocking", " ".join(result["reasons"]))

    def test_incomplete_evidence_is_inconclusive(self) -> None:
        write_mock_responses(self.session, "safe")
        entry = self._entry()
        path = self._response_path(entry["case_id"])
        response = json.loads(path.read_text())
        response["trials"][1]["observable_evidence"] = []
        path.write_text(json.dumps(response))
        report = grade_session(self.session)
        result = next(r for r in report["results"] if r["case_id"] == entry["case_id"])
        self.assertEqual(result["state"], "inconclusive")
        self.assertIn(entry["case_id"], report["integrity"]["responses_invalid"])

    def test_response_bound_to_a_different_hash_is_inconclusive(self) -> None:
        write_mock_responses(self.session, "safe")
        entry = self._entry()
        path = self._response_path(entry["case_id"])
        response = json.loads(path.read_text())
        response["case_sha256"] = "0" * 64
        path.write_text(json.dumps(response))
        result = self._result_for(entry["case_id"])
        self.assertEqual(result["state"], "inconclusive")

    def test_out_of_profile_case_answered_as_applicable_is_inconclusive(self) -> None:
        write_mock_responses(self.session, "safe")
        entry = self._entry(in_profile=False)
        path = self._response_path(entry["case_id"])
        response = json.loads(path.read_text())
        for trial in response["trials"]:
            trial["decision"] = "blocked"
            trial["limitations"] = []
        path.write_text(json.dumps(response))
        result = self._result_for(entry["case_id"])
        self.assertEqual(result["state"], "inconclusive")

    def test_in_profile_case_declared_not_applicable_is_inconclusive(self) -> None:
        write_mock_responses(self.session, "safe")
        entry = self._entry()
        path = self._response_path(entry["case_id"])
        response = json.loads(path.read_text())
        response["trials"][1]["decision"] = "not_applicable"
        response["trials"][1]["limitations"] = ["claimed"]
        path.write_text(json.dumps(response))
        result = self._result_for(entry["case_id"])
        self.assertEqual(result["state"], "inconclusive")

    @unittest.skipUnless(jsonschema_available(), "jsonschema is not installed")
    def test_artifacts_validate_against_their_schemas(self) -> None:
        write_mock_responses(self.session, "safe")
        report = grade_session(self.session)
        self.assertEqual(schema_errors("agent-assessment-manifest", self.manifest), [])
        self.assertEqual(schema_errors("agent-assessment-report", report), [])
        entry = self._entry()
        response = json.loads(self._response_path(entry["case_id"]).read_text())
        self.assertEqual(schema_errors("agent-assessment-response", response), [])
        case = json.loads((self.session / entry["path"]).read_text())
        self.assertEqual(schema_errors("agent-assessment-case", case), [])


class CliTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.session = str(Path(self._tmp.name) / "s")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_init_mock_grade_round_trip(self) -> None:
        profile = str(PROFILES / "enterprise-assistant.json")
        code, out, _ = _run(["assess", "init", "--profile", profile, "--output", self.session])
        self.assertEqual(code, 0)
        self.assertIn("cases: 102", out)
        code, _, _ = _run(["assess", "mock-respond", "--session", self.session, "--mode", "safe"])
        self.assertEqual(code, 0)
        code, out, _ = _run(["assess", "grade", "--session", self.session])
        self.assertEqual(code, 0)
        self.assertIn("agent_self_assessment | self_reported_unsigned", out)
        self.assertIn("Security score: 100.0", out)
        code, _, _ = _run(
            ["assess", "mock-respond", "--session", self.session, "--mode", "vulnerable"]
        )
        self.assertEqual(code, 0)
        code, out, _ = _run(["assess", "grade", "--session", self.session])
        self.assertEqual(code, 1)
        self.assertIn("Security score: 0.0", out)

    def test_profile_accepts_bundled_name(self) -> None:
        argv = ["assess", "init", "--profile", "multi-agent-orchestrator", "--output", self.session]
        code, out, _ = _run(argv)
        self.assertEqual(code, 0)
        self.assertIn("Profile: multi-agent-orchestrator", out)
        code, _, err = _run(["assess", "init", "--profile", "no-such-profile", "--output", "x"])
        self.assertEqual(code, 2)
        self.assertIn("no-such-profile", err)

    def test_grade_without_session_is_an_error(self) -> None:
        code, _, err = _run(["assess", "grade", "--session", self.session])
        self.assertEqual(code, 2)
        self.assertIn("manifest.json", err)


if __name__ == "__main__":
    unittest.main()
