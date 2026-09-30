from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

from .adapters import CommandAdapter, HttpAdapter, MockAdapter
from .loaders import ValidationError, discover_tests, load_data, validate_test_case
from .reports import write_html, write_json, write_junit
from .runner import BenchmarkRunner
from .scoring import score


def _repo_root() -> Path:
    current = Path.cwd()
    for candidate in (current, *current.parents):
        if (candidate / "data" / "taxonomy" / "caap-200.json").exists():
            return candidate
    return current


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
    print(f"Validated {len(files)} case(s); {failures} failed")
    return 1 if failures else 0


def _selected_cases(args: argparse.Namespace) -> list[tuple[Path, dict[str, Any]]]:
    selected: list[tuple[Path, dict[str, Any]]] = []
    for path in discover_tests(args.paths):
        case = load_data(path)
        if args.pattern and case.get("pattern_id") not in set(args.pattern):
            continue
        if args.tag and not set(args.tag).issubset(set(case.get("tags", []))):
            continue
        selected.append((path, case))
    return selected


def cmd_run(args: argparse.Namespace) -> int:
    cases = _selected_cases(args)
    if not cases:
        print("No executable test cases matched.", file=sys.stderr)
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


def build_parser() -> argparse.ArgumentParser:
    root = _repo_root()
    parser = argparse.ArgumentParser(prog="caap", description="Run safe CAAP agent benchmarks")
    parser.add_argument("--version", action="version", version="caap-benchmark 0.1.0")
    sub = parser.add_subparsers(dest="subcommand", required=True)

    listing = sub.add_parser("list", help="list CAAP-200 patterns")
    listing.add_argument("--taxonomy", default=root / "data/taxonomy/caap-200.json")
    listing.add_argument("--domain")
    listing.add_argument("--maturity", choices=["reference", "candidate", "catalog"])
    listing.set_defaults(func=cmd_list)

    show = sub.add_parser("show", help="show one taxonomy record")
    show.add_argument("pattern_id")
    show.add_argument("--taxonomy", default=root / "data/taxonomy/caap-200.json")
    show.set_defaults(func=cmd_show)

    validate = sub.add_parser("validate", help="validate benchmark test definitions")
    validate.add_argument("paths", nargs="*", default=[root / "benchmarks/executable"])
    validate.add_argument("--verbose", action="store_true")
    validate.set_defaults(func=cmd_validate)

    run = sub.add_parser("run", help="execute benchmark cases")
    run.add_argument("paths", nargs="*", default=[root / "benchmarks/executable"])
    run.add_argument("--pattern", action="append", help="stable pattern ID; repeatable")
    run.add_argument("--tag", action="append", help="required case tag; repeatable")
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
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
