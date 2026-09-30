from __future__ import annotations

import argparse
import json
import os
import sys
from importlib import resources
from pathlib import Path
from typing import Any

from .adapters import CommandAdapter, HttpAdapter, MockAdapter
from .assess import (
    AssessmentError,
    grade_session,
    import_responses,
    init_session,
    render_prompt,
    write_mock_responses,
)
from .attest import BundleError, create_bundle, verify_bundle
from .loaders import ValidationError, discover_tests, load_data, validate_test_case
from .reports import write_html, write_json, write_junit
from .runner import BenchmarkRunner
from .schemas import validator_name
from .scoring import score
from .versions import TAXONOMY_VERSION, package_version


def _repo_root() -> Path | None:
    """Return the repository checkout containing the working directory, if any."""
    current = Path.cwd()
    for candidate in (current, *current.parents):
        if (candidate / "data" / "taxonomy" / "caap-200.json").exists():
            return candidate
    return None


def default_paths() -> tuple[Path, Path]:
    """Return the default taxonomy file and executable-case directory.

    A repository checkout takes precedence so edits in progress are picked up.
    Outside a checkout the copies bundled with the package are used, which lets
    an installed `caap` list, show, validate, and run without the repository.
    """
    repo = _repo_root()
    if repo is not None:
        return repo / "data/taxonomy/caap-200.json", repo / "benchmarks/executable"
    packaged = Path(str(resources.files("caap_benchmark") / "data"))
    return packaged / "taxonomy/caap-200.json", packaged / "benchmarks/executable"


def default_assessment_paths() -> tuple[Path, Path]:
    """Return the default assessment-case and profile directories (checkout, else package)."""
    repo = _repo_root()
    if repo is not None:
        return repo / "assessments/cases", repo / "profiles"
    packaged = Path(str(resources.files("caap_benchmark") / "data"))
    return packaged / "assessments/cases", packaged / "profiles"


def _adapter(args: argparse.Namespace):
    if args.adapter == "mock":
        return MockAdapter(vulnerable=args.mock_mode == "vulnerable")
    if args.adapter == "http":
        if not args.endpoint:
            raise SystemExit("--endpoint is required for the http adapter")
        return HttpAdapter(
            args.endpoint,
            timeout=args.timeout,
            bearer_token=os.environ.get("CAAP_BEARER_TOKEN"),
            allow_remote=args.allow_remote_authorized_target,
        )
    if args.adapter == "command":
        if not args.command:
            raise SystemExit("--command is required for the command adapter")
        return CommandAdapter(args.command, timeout=args.timeout)
    raise SystemExit(f"unknown adapter: {args.adapter}")


def cmd_list(args: argparse.Namespace) -> int:
    taxonomy = load_data(args.taxonomy)
    patterns = taxonomy.get("patterns", [])
    if args.domain:
        patterns = [pattern for pattern in patterns if pattern["domain_id"] == args.domain.upper()]
    if args.maturity:
        patterns = [pattern for pattern in patterns if pattern["maturity"] == args.maturity]
    for pattern in patterns:
        marker = "executable" if pattern["implementation_status"] == "executable" else "scaffold"
        print(f"{pattern['id']:<12} {pattern['name']:<52} {marker}")
    print(f"\n{len(patterns)} pattern(s)")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    files = discover_tests(args.paths)
    failures = 0
    for path in files:
        try:
            errors = validate_test_case(load_data(path))
        except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
            errors = [str(exc)]
        if errors:
            failures += 1
            print(f"FAIL {path}")
            for error in errors:
                print(f"  - {error}")
        elif args.verbose:
            print(f"PASS {path}")
    print(f"Validated {len(files)} case(s); {failures} failed | validator: {validator_name()}")
    return 1 if failures else 0


def _selected_cases(args: argparse.Namespace) -> tuple[list[tuple[Path, dict[str, Any]]], int]:
    """Return the cases to run and the number skipped because they are disabled."""
    selected: list[tuple[Path, dict[str, Any]]] = []
    skipped_disabled = 0
    for path in discover_tests(args.paths):
        case = load_data(path)
        if args.pattern and case.get("pattern_id") not in set(args.pattern):
            continue
        if args.tag and not set(args.tag).issubset(set(case.get("tags", []))):
            continue
        if case.get("enabled", True) is False and not args.include_disabled:
            skipped_disabled += 1
            continue
        selected.append((path, case))
    return selected, skipped_disabled


def cmd_run(args: argparse.Namespace) -> int:
    cases, skipped_disabled = _selected_cases(args)
    if skipped_disabled:
        print(
            f"Skipped {skipped_disabled} disabled case(s); pass --include-disabled to run them.",
            file=sys.stderr,
        )
    if not cases:
        print("No enabled test cases matched.", file=sys.stderr)
        return 2
    runner = BenchmarkRunner(_adapter(args))
    results = []
    for path, case in cases:
        try:
            result = runner.run(case)
        except (ValidationError, OSError, ValueError) as exc:
            print(f"ERROR {path}: {exc}", file=sys.stderr)
            return 2
        results.append(result)
        print(f"{result.state.value.upper():<14} {result.pattern_id}  {result.title}")
    scorecard = score(results)
    report_dir = Path(args.report_dir)
    report_dir.mkdir(parents=True, exist_ok=True)
    write_json(report_dir / "caap-report.json", results, scorecard)
    write_html(report_dir / "caap-report.html", results, scorecard)
    write_junit(report_dir / "caap-junit.xml", results)
    security = "n/a" if scorecard.security_score is None else scorecard.security_score
    weighted = (
        "n/a" if scorecard.severity_weighted_score is None else scorecard.severity_weighted_score
    )
    print(
        f"\nSecurity score: {security} | weighted: {weighted}"
        f" | coverage: {scorecard.coverage_percent}%"
    )
    print(f"Reports: {report_dir.resolve()}")
    if args.fail_on == "fail" and scorecard.failed:
        return 1
    if args.fail_on == "non-pass" and (scorecard.total != scorecard.passed):
        return 1
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    taxonomy = load_data(args.taxonomy)
    pattern = next((item for item in taxonomy["patterns"] if item["id"] == args.pattern_id), None)
    if not pattern:
        print(f"Unknown pattern: {args.pattern_id}", file=sys.stderr)
        return 2
    print(json.dumps(pattern, indent=2))
    return 0


def _resolve_profile(value: str, profiles_dir: Path) -> Path:
    """Accept a profile path or the bare name of a bundled example profile."""
    path = Path(value)
    if path.is_file():
        return path
    candidate = Path(profiles_dir) / f"{value.removesuffix('.json')}.json"
    return candidate if candidate.is_file() else path


def cmd_assess_init(args: argparse.Namespace) -> int:
    profile = _resolve_profile(args.profile, args.profiles_dir)
    try:
        manifest = init_session(profile, args.scope, args.cases, args.output)
    except AssessmentError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    counts = manifest["counts"]
    print(
        f"Assessment session initialized at {Path(args.output).resolve()}\n"
        f"Profile: {manifest['profile']['name']} | scope: {manifest['scope']} | "
        f"cases: {counts['selected']} ({counts['in_profile']} in profile, "
        f"{counts['out_of_profile']} out of profile) | trials: {counts['trials']}\n"
        f"Manifest sha256: {manifest['manifest_sha256']}\n"
        f"Next: follow INSTRUCTIONS.md, write responses/, then run `caap assess grade`."
    )
    return 0


def cmd_assess_mock_respond(args: argparse.Namespace) -> int:
    try:
        count = write_mock_responses(args.session, args.mode)
    except AssessmentError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"Wrote {count} mock {args.mode} response(s) to {Path(args.session) / 'responses'}")
    return 0


def cmd_assess_prompt(args: argparse.Namespace) -> int:
    try:
        prompts = render_prompt(args.session, args.chunk_size)
    except AssessmentError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    base = Path(args.output) if args.output else Path(args.session) / "prompt.md"
    base.parent.mkdir(parents=True, exist_ok=True)
    for label, text in prompts:
        target = base
        if len(prompts) > 1:
            target = base.with_name(f"{base.stem}-{label[len('prompt-'):]}{base.suffix}")
        target.write_text(text, encoding="utf-8")
        print(f"{target} ({len(text.encode('utf-8'))} bytes)")
    print(
        "Give each prompt to the model under evaluation, save its reply, then run "
        "`caap assess import` and `caap assess grade`."
    )
    return 0


def cmd_assess_import(args: argparse.Namespace) -> int:
    try:
        summary = import_responses(args.session, args.files, args.responder)
    except AssessmentError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(
        f"Imported {len(summary['imported'])} response(s), replaced {len(summary['replaced'])}, "
        f"skipped {len(summary['skipped'])} into {Path(args.session) / 'responses'}"
    )
    for case_id, reason in summary["skipped"]:
        print(f"  skipped {case_id}: {reason}", file=sys.stderr)
    for error in summary["errors"]:
        print(f"ERROR: {error}", file=sys.stderr)
    if summary["errors"]:
        return 2
    return 1 if summary["skipped"] else 0


def cmd_assess_grade(args: argparse.Namespace) -> int:
    try:
        report = grade_session(args.session, args.report)
    except AssessmentError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    card = report["scorecard"]
    integrity = report["integrity"]
    for result in report["results"]:
        marker = "" if result["in_profile"] else "  (out of profile)"
        print(f"{result['state'].upper():<14} {result['pattern_id']}{marker}")
    print(
        f"\n{report['assessment_kind']} | {report['assurance']} | profile: {report['profile_name']}"
        f" | scope: {report['scope']}"
    )
    score = card["security_score"]
    weighted = card["severity_weighted_score"]
    print(
        f"Security score: {score if score is not None else 'n/a'}"
        f" | weighted: {weighted if weighted is not None else 'n/a'}"
        f" | coverage: {card['coverage_percent']}% | over-blocking: {card['over_blocking_count']}"
        f" | recovery verified: {card['recovery_verified_percent']}%"
    )
    for layer, summary in report["layers"].items():
        score = summary["security_score"] if summary["security_score"] is not None else "n/a"
        print(
            f"  {layer:<12} cases {summary['cases']:>3}  pass {summary['passed']:>3}"
            f"  fail {summary['failed']:>3}  inconclusive {summary['inconclusive']:>3}"
            f"  n/a {summary['not_applicable']:>3}  score {score}"
        )
    if not integrity["manifest_verified"]:
        print("WARNING: manifest hash does not verify", file=sys.stderr)
    if integrity["cases_tampered"]:
        print(f"WARNING: tampered cases: {', '.join(integrity['cases_tampered'])}", file=sys.stderr)
    if integrity["responses_missing"]:
        print(f"Missing responses: {len(integrity['responses_missing'])}", file=sys.stderr)
    report_path = Path(args.report) if args.report else Path(args.session) / "report.json"
    print(f"Report: {report_path.resolve()}")
    blocked = (
        card["failed"] > 0
        or bool(integrity["cases_tampered"])
        or not integrity["manifest_verified"]
    )
    if args.fail_on == "fail" and blocked:
        return 1
    if args.fail_on == "non-pass" and (card["total"] != card["passed"] + card["not_applicable"]):
        return 1
    return 0


def cmd_attest_create(args: argparse.Namespace) -> int:
    subject = {
        "name": args.subject,
        "version": args.subject_version,
        "description": args.subject_description,
    }
    try:
        submission = create_bundle(
            args.output,
            subject,
            session=args.session,
            report=args.report,
            authorization_statement=args.authorization,
            notes=args.notes,
        )
    except BundleError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    card = submission["scorecard"]
    print(
        f"Evidence bundle written to {Path(args.output).resolve()}\n"
        f"Tier: {submission['assurance_tier']} ({', '.join(submission['labels'])})\n"
        f"Subject: {submission['subject']['name']} {submission['subject']['version'] or ''}\n"
        f"Taxonomy {submission['taxonomy_version']} | benchmark "
        f"{submission['caap_benchmark_version']} | cases {submission['evaluation']['case_count']}"
        f" | security score {card['security_score']} | coverage {card['coverage_percent']}%\n"
        f"Badge: {submission['badge']['label']} | {submission['badge']['message']}\n"
        f"Submission sha256: {submission['submission_sha256']}\n"
        f"Verify with `caap attest verify {args.output}` before submitting."
    )
    return 0


def cmd_attest_verify(args: argparse.Namespace) -> int:
    try:
        outcome = verify_bundle(args.bundle)
    except BundleError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(outcome, indent=2))
        return 0 if outcome["verified"] else 1
    for check in outcome["checks"]:
        print(f"{check['status'].upper():<5} {check['name']}: {check['detail']}")
    submission = outcome["submission"]
    if outcome["tier"]:
        print(
            f"\n{submission['subject']['name']} | {outcome['tier']} | "
            f"taxonomy {submission['taxonomy_version']} | "
            f"security score {submission['scorecard']['security_score']} | "
            f"coverage {submission['scorecard']['coverage_percent']}%"
        )
    print("VERIFIED" if outcome["verified"] else "NOT VERIFIED")
    return 0 if outcome["verified"] else 1


def build_parser() -> argparse.ArgumentParser:
    taxonomy_path, executable_dir = default_paths()
    assessment_cases_dir, profiles_dir = default_assessment_paths()
    parser = argparse.ArgumentParser(prog="caap", description="Run safe CAAP agent benchmarks")
    parser.add_argument(
        "--version",
        action="version",
        version=f"caap-benchmark {package_version()} (CAAP-200 taxonomy {TAXONOMY_VERSION})",
    )
    sub = parser.add_subparsers(dest="subcommand", required=True)

    listing = sub.add_parser("list", help="list CAAP-200 patterns")
    listing.add_argument("--taxonomy", default=taxonomy_path)
    listing.add_argument("--domain")
    listing.add_argument("--maturity", choices=["reference", "candidate", "catalog"])
    listing.set_defaults(func=cmd_list)

    show = sub.add_parser("show", help="show one taxonomy record")
    show.add_argument("pattern_id")
    show.add_argument("--taxonomy", default=taxonomy_path)
    show.set_defaults(func=cmd_show)

    validate = sub.add_parser("validate", help="validate benchmark test definitions")
    validate.add_argument("paths", nargs="*", default=[executable_dir])
    validate.add_argument("--verbose", action="store_true")
    validate.set_defaults(func=cmd_validate)

    run = sub.add_parser("run", help="execute benchmark cases")
    run.add_argument("paths", nargs="*", default=[executable_dir])
    run.add_argument("--pattern", action="append", help="stable pattern ID; repeatable")
    run.add_argument("--tag", action="append", help="required case tag; repeatable")
    run.add_argument(
        "--include-disabled",
        action="store_true",
        help="also run cases marked enabled: false, such as contributor scaffolds",
    )
    run.add_argument("--adapter", choices=["mock", "http", "command"], default="mock")
    run.add_argument("--mock-mode", choices=["safe", "vulnerable"], default="safe")
    run.add_argument("--endpoint", help="authorized test endpoint for the HTTP adapter")
    run.add_argument(
        "--allow-remote-authorized-target",
        action="store_true",
        help="confirm that a non-local endpoint is explicitly authorized for this test",
    )
    run.add_argument("--command", help="explicit local adapter command")
    run.add_argument("--timeout", type=float, default=30.0)
    run.add_argument("--report-dir", default="reports")
    run.add_argument("--fail-on", choices=["never", "fail", "non-pass"], default="fail")
    run.set_defaults(func=cmd_run)

    assess = sub.add_parser("assess", help="agent-native CAAP-200 assessment (adapter-free)")
    assess_sub = assess.add_subparsers(dest="assess_command", required=True)

    init = assess_sub.add_parser("init", help="create a hash-bound assessment session")
    init.add_argument(
        "--profile",
        required=True,
        help=(
            "capability profile JSON path, or the name of a bundled example "
            f"profile from {profiles_dir}"
        ),
    )
    init.add_argument("--scope", choices=["applicable", "full"], default="applicable")
    init.add_argument("--cases", default=assessment_cases_dir, help="assessment case directory")
    init.add_argument("--profiles-dir", default=profiles_dir, help=argparse.SUPPRESS)
    init.add_argument("--output", default=".caap/assessment", help="session directory to create")
    init.set_defaults(func=cmd_assess_init)

    mock = assess_sub.add_parser(
        "mock-respond", help="write deterministic mock responses to validate the protocol"
    )
    mock.add_argument("--session", required=True)
    mock.add_argument("--mode", choices=["safe", "vulnerable"], default="safe")
    mock.set_defaults(func=cmd_assess_mock_respond)

    prompt = assess_sub.add_parser(
        "prompt", help="render the session as a self-contained prompt for any LLM"
    )
    prompt.add_argument("--session", required=True)
    prompt.add_argument("--output", help="prompt path (default: <session>/prompt.md)")
    prompt.add_argument(
        "--chunk-size",
        type=int,
        help="split into numbered prompts of at most this many cases each",
    )
    prompt.set_defaults(func=cmd_assess_prompt)

    imp = assess_sub.add_parser(
        "import", help="import a model's JSON reply (or Markdown with a json block) as responses"
    )
    imp.add_argument("--session", required=True)
    imp.add_argument("files", nargs="+", help="reply files saved from the model")
    imp.add_argument("--responder", help="responder label to record when the reply omits one")
    imp.set_defaults(func=cmd_assess_import)

    grade = assess_sub.add_parser("grade", help="verify hashes, grade responses, write the report")
    grade.add_argument("--session", required=True)
    grade.add_argument("--report", help="report path (default: <session>/report.json)")
    grade.add_argument("--fail-on", choices=["never", "fail", "non-pass"], default="fail")
    grade.set_defaults(func=cmd_assess_grade)

    attest = sub.add_parser("attest", help="package a result as an evidence bundle, or verify one")
    attest_sub = attest.add_subparsers(dest="attest_command", required=True)

    create = attest_sub.add_parser("create", help="write an evidence bundle from a result")
    source = create.add_mutually_exclusive_group(required=True)
    source.add_argument("--session", help="graded agent-native assessment session directory")
    source.add_argument("--report", help="observed benchmark report JSON from `caap run`")
    create.add_argument("--subject", required=True, help="name of the agent that was evaluated")
    create.add_argument("--subject-version", help="version of the evaluated agent")
    create.add_argument("--subject-description", help="one sentence describing the subject")
    create.add_argument("--authorization", help="authorization statement for the evaluation")
    create.add_argument("--notes", help="free-text notes recorded in the submission")
    create.add_argument("--output", default="caap-evidence.zip", help="bundle path to write")
    create.set_defaults(func=cmd_attest_create)

    verify = attest_sub.add_parser("verify", help="verify an evidence bundle's hashes and results")
    verify.add_argument("bundle")
    verify.add_argument("--json", action="store_true", help="print the verification as JSON")
    verify.set_defaults(func=cmd_attest_verify)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
