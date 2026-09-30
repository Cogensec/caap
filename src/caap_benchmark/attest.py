"""Evidence bundles: package a CAAP result for public submission and verify one.

`create_bundle` turns an agent-native assessment session or an observed benchmark
report into a single `caap-evidence.zip` whose `submission.json` names the
assurance tier, the versions, the subject, the scorecard, every evidence file
with its SHA-256, and its own canonical hash. `verify_bundle` is the reference
verifier a registry or a third party runs: it checks every hash, re-grades an
assessment from the bundled responses, recomputes an observed scorecard from the
bundled results, and reports each check. The bundle format is specified in
docs/EVIDENCE_SUBMISSION.md and schemas/evidence-bundle.schema.json.
"""

from __future__ import annotations

import hashlib
import json
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .assess import (
    ASSESSMENT_KIND,
    ASSURANCE,
    CLAIM_BOUNDARY,
    AssessmentError,
    canonical_sha256,
    grade_session,
    load_manifest,
    manifest_verified,
)
from .models import ResultState, RunResult
from .schemas import load_schema, schema_errors
from .scoring import score
from .versions import TAXONOMY_VERSION, package_version

BUNDLE_KIND = "caap-evidence-bundle"
SUBMISSION_FILE = "submission.json"
EVIDENCE_DIR = "evidence"
TIERS = {
    "agent_native": {
        "kind": ASSESSMENT_KIND,
        "labels": [ASSESSMENT_KIND, ASSURANCE],
        "badge": "self-assessed",
        "claim_boundary": CLAIM_BOUNDARY,
    },
    "observed_reference": {
        "kind": "observed_reference",
        "labels": ["observed_reference", "reproducible_unsigned"],
        "badge": "observed",
        "claim_boundary": (
            "Observed reference results are reproducible from the normalized events and "
            "telemetry the adapter recorded, and every result carries an evidence digest. "
            "They are not independently verified: the operator controlled the target, the "
            "adapter, and the run. They are engineering evidence, not certification."
        ),
    },
}
CLAIM_RULE = (
    "A public CAAP claim MUST state the assurance tier, the taxonomy version, the profile "
    "and scope (agent-native) or the adapter (observed), the security score, and the "
    "coverage together. A score shown without its tier, version, and coverage is not a "
    "CAAP claim. Independent verification is not offered by this repository."
)


class BundleError(ValueError):
    """The bundle could not be created or read."""


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _read_json_bytes(data: bytes, label: str) -> Any:
    try:
        return json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise BundleError(f"{label}: not valid JSON ({exc})") from exc


def badge_for(tier: str, case_count: int, taxonomy_version: str) -> dict[str, str]:
    return {
        "label": "CAAP-200",
        "message": f"{TIERS[tier]['badge']} · {case_count} cases · {taxonomy_version}",
        "tier": tier,
    }


# ---------------------------------------------------------------------------
# Creation
# ---------------------------------------------------------------------------


def _collect_session(session: Path) -> tuple[dict[str, Any], dict[str, Path]]:
    manifest = load_manifest(session)
    report_path = session / "report.json"
    if not report_path.is_file():
        raise BundleError(f"no report.json in {session}; run `caap assess grade` first")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    if report.get("manifest_sha256") != manifest["manifest_sha256"]:
        raise BundleError("report.json was graded against a different manifest; re-run grade")
    files: dict[str, Path] = {
        f"{EVIDENCE_DIR}/manifest.json": session / "manifest.json",
        f"{EVIDENCE_DIR}/report.json": report_path,
    }
    for entry in manifest["cases"]:
        case_path = session / entry["path"]
        if not case_path.is_file():
            raise BundleError(f"case file missing from session: {entry['path']}")
        files[f"{EVIDENCE_DIR}/{entry['path']}"] = case_path
        response_path = session / "responses" / f"{entry['case_id']}.json"
        if response_path.is_file():
            files[f"{EVIDENCE_DIR}/responses/{entry['case_id']}.json"] = response_path
    evaluation = {
        "kind": ASSESSMENT_KIND,
        "case_count": len(manifest["cases"]),
        "profile": {
            "name": manifest["profile"]["name"],
            "capabilities": list(manifest["profile"]["capabilities"]),
        },
        "scope": manifest["scope"],
        "manifest_sha256": manifest["manifest_sha256"],
    }
    submission = {
        "assurance_tier": "agent_native",
        "taxonomy_version": manifest["taxonomy_version"],
        "caap_benchmark_version": manifest["caap_benchmark_version"],
        "evaluation": evaluation,
        "scorecard": report["scorecard"],
        "layers": report["layers"],
        "integrity": report["integrity"],
    }
    return submission, files


def _collect_report(report_path: Path) -> tuple[dict[str, Any], dict[str, Path]]:
    if not report_path.is_file():
        raise BundleError(f"report not found: {report_path}")
    report = _read_json_bytes(report_path.read_bytes(), report_path.name)
    errors = _document_errors("report", report)
    if not errors and not isinstance(report.get("results"), list):
        errors = ["results must be an array"]
    if errors:
        raise BundleError("invalid benchmark report: " + "; ".join(errors[:3]))
    results = report["results"]
    if not results:
        raise BundleError("the report contains no results")
    adapters = sorted({str(result.get("adapter", "unknown")) for result in results})
    digests = sum(1 for result in results if result.get("evidence", {}).get("sha256"))
    submission = {
        "assurance_tier": "observed_reference",
        "taxonomy_version": report.get("taxonomy_version", TAXONOMY_VERSION),
        "caap_benchmark_version": report.get("caap_benchmark_version", package_version()),
        "evaluation": {
            "kind": "observed_reference",
            "case_count": len(results),
            "adapters": adapters,
        },
        "scorecard": report["scorecard"],
        "layers": None,
        "integrity": {"results": len(results), "results_with_evidence_digest": digests},
    }
    return submission, {f"{EVIDENCE_DIR}/report.json": report_path}


def create_bundle(
    output: str | Path,
    subject: dict[str, Any],
    session: str | Path | None = None,
    report: str | Path | None = None,
    authorization_statement: str | None = None,
    notes: str | None = None,
) -> dict[str, Any]:
    """Write `output` (a zip) from an assessment session or an observed report."""
    if (session is None) == (report is None):
        raise BundleError("provide exactly one of session or report")
    if not subject.get("name"):
        raise BundleError("subject name is required")
    try:
        body, files = _collect_session(Path(session)) if session else _collect_report(Path(report))
    except AssessmentError as exc:
        raise BundleError(str(exc)) from exc
    tier = body["assurance_tier"]
    file_entries = []
    payloads: dict[str, bytes] = {}
    for archive_path, source in sorted(files.items()):
        data = source.read_bytes()
        payloads[archive_path] = data
        file_entries.append(
            {"path": archive_path, "sha256": _sha256_bytes(data), "bytes": len(data)}
        )
    submission: dict[str, Any] = {
        "schema_version": "1.0",
        "bundle_kind": BUNDLE_KIND,
        "generated_at": _now(),
        "assurance_tier": tier,
        "labels": list(TIERS[tier]["labels"]),
        "taxonomy_version": body["taxonomy_version"],
        "caap_benchmark_version": body["caap_benchmark_version"],
        "subject": {
            "name": str(subject["name"]),
            "version": subject.get("version"),
            "description": subject.get("description"),
        },
        "evaluation": body["evaluation"],
        "scorecard": body["scorecard"],
        "layers": body["layers"],
        "integrity": body["integrity"],
        "authorization_statement": authorization_statement,
        "notes": notes,
        "claim_boundary": TIERS[tier]["claim_boundary"],
        "claim_rule": CLAIM_RULE,
        "badge": badge_for(tier, body["evaluation"]["case_count"], body["taxonomy_version"]),
        "files": file_entries,
    }
    submission["submission_sha256"] = canonical_sha256(submission)
    errors = schema_errors("evidence-bundle", submission)
    if errors:
        raise BundleError("internal error: submission fails its schema: " + "; ".join(errors[:3]))
    target = Path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(SUBMISSION_FILE, json.dumps(submission, indent=2) + "\n")
        for archive_path, data in payloads.items():
            archive.writestr(archive_path, data)
    return submission


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------


def _check(checks: list[dict[str, str]], name: str, ok: bool, detail: str) -> bool:
    checks.append({"name": name, "status": "pass" if ok else "fail", "detail": detail})
    return ok


def _warn(checks: list[dict[str, str]], name: str, detail: str) -> None:
    checks.append({"name": name, "status": "warn", "detail": detail})


def _read_bundle(path: Path) -> tuple[dict[str, Any], dict[str, bytes]]:
    if not path.is_file():
        raise BundleError(f"bundle not found: {path}")
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            if SUBMISSION_FILE not in names:
                raise BundleError(f"{path.name}: no {SUBMISSION_FILE} in bundle")
            contents = {name: archive.read(name) for name in names if not name.endswith("/")}
    except zipfile.BadZipFile as exc:
        raise BundleError(f"{path.name}: not a zip file") from exc
    submission = _read_json_bytes(contents.pop(SUBMISSION_FILE), SUBMISSION_FILE)
    return submission, contents


def _document_errors(schema_name: str, document: Any) -> list[str]:
    """Schema-validate a bundled document, falling back to its required keys."""
    errors = schema_errors(schema_name, document)
    if errors is not None:
        return errors
    if not isinstance(document, dict):
        return [f"{schema_name}: must be an object"]
    required = load_schema(schema_name).get("required", [])
    return [f"missing required field: {key}" for key in required if key not in document]


def _structural_submission_errors(submission: Any) -> list[str]:
    if not isinstance(submission, dict):
        return ["submission must be an object"]
    errors = []
    for key in load_schema("evidence-bundle")["required"]:
        if key not in submission:
            errors.append(f"missing required field: {key}")
    if submission.get("bundle_kind") != BUNDLE_KIND:
        errors.append("bundle_kind must be caap-evidence-bundle")
    if submission.get("assurance_tier") not in TIERS:
        errors.append("assurance_tier must be one of " + ", ".join(TIERS))
    if not isinstance(submission.get("files"), list) or not submission.get("files"):
        errors.append("files must be a non-empty array")
    return errors


def _regrade_assessment(contents: dict[str, bytes]) -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for archive_path, data in contents.items():
            relative = Path(archive_path).relative_to(EVIDENCE_DIR)
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        (root / "responses").mkdir(exist_ok=True)
        return grade_session(root, root / "regraded-report.json")


def _recompute_observed(report: dict[str, Any]) -> dict[str, Any]:
    results = []
    for item in report["results"]:
        known = RunResult.__dataclass_fields__
        fields = {key: value for key, value in item.items() if key in known}
        fields["state"] = ResultState(item["state"])
        results.append(RunResult(**fields))
    return score(results).to_dict()


def verify_bundle(path: str | Path) -> dict[str, Any]:
    """Verify a bundle and return {verified, tier, checks, submission}."""
    bundle_path = Path(path)
    submission, contents = _read_bundle(bundle_path)
    checks: list[dict[str, str]] = []
    errors = schema_errors("evidence-bundle", submission)
    if errors is None:
        errors = _structural_submission_errors(submission)
        _warn(checks, "schema", "jsonschema not installed; structural check only")
    if not _check(checks, "submission_schema", not errors, "; ".join(errors[:3]) or "valid"):
        return {"verified": False, "tier": None, "checks": checks, "submission": submission}

    body = {k: v for k, v in submission.items() if k != "submission_sha256"}
    _check(
        checks,
        "submission_hash",
        canonical_sha256(body) == submission["submission_sha256"],
        "submission.json canonical hash",
    )
    declared = {entry["path"]: entry for entry in submission["files"]}
    all_present = True
    for archive_path, entry in declared.items():
        data = contents.get(archive_path)
        ok = (
            data is not None
            and _sha256_bytes(data) == entry["sha256"]
            and len(data) == entry["bytes"]
        )
        if not ok:
            all_present = False
            _check(checks, f"file:{archive_path}", False, "missing or hash/size mismatch")
    _check(checks, "files_declared", all_present, f"{len(declared)} evidence file(s) verified")
    extra = sorted(set(contents) - set(declared))
    _check(checks, "no_undeclared_files", not extra, ", ".join(extra) or "none")
    if submission["taxonomy_version"] != TAXONOMY_VERSION:
        _warn(
            checks,
            "taxonomy_version",
            f"bundle is for {submission['taxonomy_version']}; this verifier knows "
            f"{TAXONOMY_VERSION}",
        )
    tier = submission["assurance_tier"]
    _check(
        checks,
        "labels",
        submission["labels"] == TIERS[tier]["labels"],
        "tier labels match the assurance tier",
    )
    _check(
        checks,
        "claim_boundary",
        submission["claim_boundary"] == TIERS[tier]["claim_boundary"],
        "claim boundary text is the published text for the tier",
    )
    badge = badge_for(tier, submission["evaluation"]["case_count"], submission["taxonomy_version"])
    _check(checks, "badge", submission["badge"] == badge, badge["message"])

    report_bytes = contents.get(f"{EVIDENCE_DIR}/report.json")
    if report_bytes is None:
        _check(checks, "report_present", False, "evidence/report.json missing")
        return _finish(checks, tier, submission)
    try:
        report = _read_json_bytes(report_bytes, "evidence/report.json")
    except BundleError as exc:
        _check(checks, "report_schema", False, str(exc))
        return _finish(checks, tier, submission)
    schema_name = "agent-assessment-report" if tier == "agent_native" else "report"
    report_errors = _document_errors(schema_name, report)
    detail = "; ".join(report_errors[:3]) or "valid"
    if not _check(checks, "report_schema", not report_errors, detail):
        return _finish(checks, tier, submission)
    _check(
        checks,
        "scorecard_matches_report",
        submission["scorecard"] == report.get("scorecard"),
        "submission scorecard equals the bundled report",
    )
    if tier == "agent_native":
        _verify_assessment(checks, submission, contents, report)
    else:
        _verify_observed(checks, submission, report)
    return _finish(checks, tier, submission)


def _verify_assessment(
    checks: list[dict[str, str]],
    submission: dict[str, Any],
    contents: dict[str, bytes],
    report: dict[str, Any],
) -> None:
    manifest_bytes = contents.get(f"{EVIDENCE_DIR}/manifest.json")
    if manifest_bytes is None:
        _check(checks, "manifest_present", False, "evidence/manifest.json missing")
        return
    manifest = _read_json_bytes(manifest_bytes, "evidence/manifest.json")
    _check(checks, "manifest_hash", manifest_verified(manifest), "manifest canonical hash")
    _check(
        checks,
        "manifest_matches_submission",
        manifest.get("manifest_sha256") == submission["evaluation"].get("manifest_sha256"),
        "submission names the bundled manifest",
    )
    tampered = []
    for entry in manifest.get("cases", []):
        data = contents.get(f"{EVIDENCE_DIR}/{entry['path']}")
        case = _read_json_bytes(data, entry["path"]) if data is not None else None
        if case is None or canonical_sha256(case) != entry["sha256"]:
            tampered.append(entry["case_id"])
    _check(checks, "case_hashes", not tampered, ", ".join(tampered) or "every case matches")
    try:
        regraded = _regrade_assessment(contents)
    except AssessmentError as exc:
        _check(checks, "regrade", False, str(exc))
        return
    same_scorecard = regraded["scorecard"] == report["scorecard"]
    same_layers = regraded["layers"] == report["layers"]
    same_states = [r["state"] for r in regraded["results"]] == [
        r["state"] for r in report["results"]
    ]
    _check(
        checks,
        "regrade",
        same_scorecard and same_layers and same_states,
        "re-grading the bundled responses reproduces the scorecard, layers, and states",
    )
    _check(
        checks,
        "not_tampered",
        not report["integrity"].get("cases_tampered")
        and report["integrity"].get("manifest_verified") is True,
        "graded session had a verified manifest and no tampered case",
    )


def _verify_observed(
    checks: list[dict[str, str]], submission: dict[str, Any], report: dict[str, Any]
) -> None:
    try:
        recomputed = _recompute_observed(report)
    except (KeyError, TypeError, ValueError) as exc:
        _check(checks, "scorecard_recomputed", False, f"results are not gradable: {exc}")
        return
    _check(
        checks,
        "scorecard_recomputed",
        recomputed == report["scorecard"],
        "scorecard recomputed from the bundled results",
    )
    missing = [r["test_id"] for r in report["results"] if not r.get("evidence", {}).get("sha256")]
    _check(checks, "evidence_digests", not missing, ", ".join(missing) or "every result has one")
    _check(
        checks,
        "case_count",
        submission["evaluation"]["case_count"] == len(report["results"]),
        f"{len(report['results'])} result(s)",
    )


def _finish(checks: list[dict[str, str]], tier: str, submission: dict[str, Any]) -> dict:
    verified = all(check["status"] != "fail" for check in checks)
    return {"verified": verified, "tier": tier, "checks": checks, "submission": submission}
