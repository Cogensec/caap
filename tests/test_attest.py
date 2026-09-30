from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from caap_benchmark.assess import grade_session, init_session, write_mock_responses
from caap_benchmark.attest import (
    CLAIM_RULE,
    TIERS,
    BundleError,
    create_bundle,
    verify_bundle,
)
from caap_benchmark.cli import main
from caap_benchmark.schemas import jsonschema_available, schema_errors

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "assessments/cases"
PROFILES = ROOT / "profiles"
SUBJECT = {"name": "Example Agent", "version": "1.2", "description": "test subject"}


def _run(argv: list[str]) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main(argv)
    return code, out.getvalue(), err.getvalue()


def _rewrite(bundle: Path, edits: dict[str, bytes | None]) -> None:
    """Rewrite a zip, replacing (bytes) or removing (None) the named members."""
    with zipfile.ZipFile(bundle) as archive:
        contents = {name: archive.read(name) for name in archive.namelist()}
    for name, data in edits.items():
        if data is None:
            contents.pop(name, None)
        else:
            contents[name] = data
    with zipfile.ZipFile(bundle, "w") as archive:
        for name, data in contents.items():
            archive.writestr(name, data)


def _failed(outcome: dict) -> list[str]:
    return [check["name"] for check in outcome["checks"] if check["status"] == "fail"]


class AssessmentBundleTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.session = self.root / "session"
        init_session(PROFILES / "chat-assistant.json", "applicable", CASES, self.session)
        write_mock_responses(self.session, "safe")
        grade_session(self.session)
        self.bundle = self.root / "caap-evidence.zip"
        self.submission = create_bundle(self.bundle, SUBJECT, session=self.session)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_bundle_describes_the_result_and_verifies(self) -> None:
        sub = self.submission
        self.assertEqual(sub["assurance_tier"], "agent_native")
        self.assertEqual(sub["labels"], ["agent_self_assessment", "self_reported_unsigned"])
        self.assertEqual(sub["evaluation"]["case_count"], 37)
        self.assertEqual(sub["evaluation"]["profile"]["name"], "chat-assistant")
        self.assertEqual(sub["scorecard"]["security_score"], 100.0)
        self.assertEqual(sub["badge"]["message"], "self-assessed · 37 cases · 2.0.0-draft.1")
        self.assertEqual(sub["claim_rule"], CLAIM_RULE)
        self.assertEqual(sub["claim_boundary"], TIERS["agent_native"]["claim_boundary"])
        paths = {entry["path"] for entry in sub["files"]}
        self.assertIn("evidence/manifest.json", paths)
        self.assertIn("evidence/report.json", paths)
        self.assertEqual(sum(p.startswith("evidence/cases/") for p in paths), 37)
        self.assertEqual(sum(p.startswith("evidence/responses/") for p in paths), 37)
        outcome = verify_bundle(self.bundle)
        self.assertTrue(outcome["verified"], _failed(outcome))
        names = {check["name"] for check in outcome["checks"]}
        self.assertIn("regrade", names)
        self.assertIn("case_hashes", names)

    @unittest.skipUnless(jsonschema_available(), "jsonschema not installed")
    def test_submission_matches_the_published_schema(self) -> None:
        self.assertEqual(schema_errors("evidence-bundle", self.submission), [])

    def test_tampered_response_fails_regrade(self) -> None:
        member = "evidence/responses/CAAP-GH-01-ASSESS-001.json"
        with zipfile.ZipFile(self.bundle) as archive:
            response = json.loads(archive.read(member))
        response["trials"][1]["decision"] = "performed"
        _rewrite(self.bundle, {member: json.dumps(response).encode()})
        outcome = verify_bundle(self.bundle)
        self.assertFalse(outcome["verified"])
        self.assertIn("files_declared", _failed(outcome))
        self.assertIn("regrade", _failed(outcome))

    def test_edited_submission_fails_its_hash(self) -> None:
        with zipfile.ZipFile(self.bundle) as archive:
            submission = json.loads(archive.read("submission.json"))
        submission["scorecard"]["security_score"] = 99.0
        _rewrite(self.bundle, {"submission.json": json.dumps(submission).encode()})
        outcome = verify_bundle(self.bundle)
        self.assertFalse(outcome["verified"])
        self.assertIn("submission_hash", _failed(outcome))
        self.assertIn("scorecard_matches_report", _failed(outcome))

    def test_undeclared_and_missing_files_are_reported(self) -> None:
        _rewrite(
            self.bundle,
            {"evidence/extra.txt": b"x", "evidence/responses/CAAP-GH-02-ASSESS-001.json": None},
        )
        outcome = verify_bundle(self.bundle)
        self.assertFalse(outcome["verified"])
        self.assertIn("no_undeclared_files", _failed(outcome))
        self.assertIn("files_declared", _failed(outcome))

    def test_bundle_refuses_ungraded_or_stale_session(self) -> None:
        fresh = self.root / "fresh"
        init_session(PROFILES / "chat-assistant.json", "applicable", CASES, fresh)
        with self.assertRaises(BundleError):
            create_bundle(self.root / "x.zip", SUBJECT, session=fresh)
        with self.assertRaises(BundleError):
            create_bundle(self.root / "y.zip", {"name": ""}, session=self.session)
        with self.assertRaises(BundleError):
            create_bundle(self.root / "z.zip", SUBJECT)

    def test_not_a_bundle(self) -> None:
        bogus = self.root / "bogus.zip"
        bogus.write_bytes(b"not a zip")
        with self.assertRaises(BundleError):
            verify_bundle(bogus)
        with zipfile.ZipFile(bogus, "w") as archive:
            archive.writestr("readme.txt", "hello")
        with self.assertRaises(BundleError):
            verify_bundle(bogus)


class ObservedBundleTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        code, _, err = _run(
            ["run", "--adapter", "mock", "--mock-mode", "safe", "--report-dir", str(self.root)]
        )
        self.assertEqual(code, 0, err)
        self.report = self.root / "caap-report.json"
        self.bundle = self.root / "observed.zip"
        self.submission = create_bundle(self.bundle, SUBJECT, report=self.report)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_observed_bundle_verifies(self) -> None:
        sub = self.submission
        self.assertEqual(sub["assurance_tier"], "observed_reference")
        self.assertEqual(sub["labels"], ["observed_reference", "reproducible_unsigned"])
        self.assertEqual(sub["evaluation"]["adapters"], ["mock"])
        self.assertEqual(sub["evaluation"]["case_count"], 25)
        self.assertEqual(sub["taxonomy_version"], "2.0.0-draft.1")
        self.assertIsNone(sub["layers"])
        self.assertEqual([entry["path"] for entry in sub["files"]], ["evidence/report.json"])
        outcome = verify_bundle(self.bundle)
        self.assertTrue(outcome["verified"], _failed(outcome))
        names = {check["name"] for check in outcome["checks"]}
        self.assertIn("scorecard_recomputed", names)
        self.assertIn("evidence_digests", names)

    def test_report_carries_versions(self) -> None:
        report = json.loads(self.report.read_text())
        self.assertEqual(report["taxonomy_version"], "2.0.0-draft.1")
        self.assertTrue(report["caap_benchmark_version"])

    def test_edited_result_fails_recomputation(self) -> None:
        report = json.loads(self.report.read_text())
        report["results"][0]["state"] = "fail"
        _rewrite(self.bundle, {"evidence/report.json": json.dumps(report).encode()})
        outcome = verify_bundle(self.bundle)
        self.assertFalse(outcome["verified"])
        self.assertIn("files_declared", _failed(outcome))
        self.assertIn("scorecard_recomputed", _failed(outcome))

    def test_vulnerable_run_bundles_honestly(self) -> None:
        vulnerable = self.root / "vulnerable"
        argv = ["run", "--adapter", "mock", "--mock-mode", "vulnerable"]
        code, _, _ = _run(argv + ["--report-dir", str(vulnerable)])
        self.assertEqual(code, 1)
        bundle = self.root / "vulnerable.zip"
        sub = create_bundle(bundle, SUBJECT, report=vulnerable / "caap-report.json")
        self.assertEqual(sub["scorecard"]["security_score"], 0.0)
        self.assertTrue(verify_bundle(bundle)["verified"])


class CliTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_create_and_verify_round_trip(self) -> None:
        session = self.root / "s"
        init_session(PROFILES / "chat-assistant.json", "applicable", CASES, session)
        write_mock_responses(session, "safe")
        grade_session(session)
        bundle = self.root / "b.zip"
        code, out, err = _run(
            [
                "attest", "create", "--session", str(session), "--subject", "Example Agent",
                "--subject-version", "1.2", "--output", str(bundle),
            ]
        )
        self.assertEqual(code, 0, err)
        self.assertIn("Tier: agent_native", out)
        self.assertIn("self-assessed · 37 cases", out)
        code, out, _ = _run(["attest", "verify", str(bundle)])
        self.assertEqual(code, 0)
        self.assertIn("VERIFIED", out)
        self.assertNotIn("NOT VERIFIED", out)
        code, out, _ = _run(["attest", "verify", str(bundle), "--json"])
        self.assertEqual(code, 0)
        self.assertTrue(json.loads(out)["verified"])
        _rewrite(bundle, {"evidence/report.json": b"{}"})
        code, out, _ = _run(["attest", "verify", str(bundle)])
        self.assertEqual(code, 1)
        self.assertIn("NOT VERIFIED", out)

    def test_missing_inputs_are_errors(self) -> None:
        code, _, err = _run(
            ["attest", "create", "--report", str(self.root / "none.json"), "--subject", "x"]
        )
        self.assertEqual(code, 2)
        self.assertIn("report not found", err)
        code, _, err = _run(["attest", "verify", str(self.root / "none.zip")])
        self.assertEqual(code, 2)
        self.assertIn("bundle not found", err)


if __name__ == "__main__":
    unittest.main()
