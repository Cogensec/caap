#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_DATA = ROOT / "src" / "caap_benchmark" / "data"

sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from caap_benchmark.schemas import schema_errors  # noqa: E402

EXPECTED = {
    "GH": 22, "TM": 24, "IP": 20, "SC": 20, "CE": 15, "MP": 21,
    "IA": 19, "CF": 16, "HT": 15, "RA": 16, "EA": 12,
}
REFERENCE_IDS = {
    "CAAP-CE-01", "CAAP-CE-05", "CAAP-CF-01", "CAAP-EA-03", "CAAP-GH-01",
    "CAAP-GH-02", "CAAP-GH-03", "CAAP-GH-05", "CAAP-HT-04", "CAAP-IA-01",
    "CAAP-IA-03", "CAAP-IP-01", "CAAP-IP-02", "CAAP-IP-05", "CAAP-MP-01",
    "CAAP-MP-02", "CAAP-MP-04", "CAAP-RA-05", "CAAP-SC-01", "CAAP-SC-02",
    "CAAP-SC-04", "CAAP-TM-01", "CAAP-TM-03", "CAAP-TM-05", "CAAP-TM-06",
}
ID_PATTERN = re.compile(r"CAAP-(GH|TM|IP|SC|CE|MP|IA|CF|HT|RA|EA)-\d{2}")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    registry = json.loads((ROOT / "data/taxonomy/caap-200.json").read_text())
    patterns = registry["patterns"]
    if len(patterns) != 200:
        fail(f"expected 200 patterns, got {len(patterns)}")
    ids = [pattern["id"] for pattern in patterns]
    if len(ids) != len(set(ids)):
        fail("pattern IDs are not unique")
    if any(not ID_PATTERN.fullmatch(value) for value in ids):
        fail("invalid stable ID")
    domains = Counter(pattern["domain_id"] for pattern in patterns)
    if dict(domains) != EXPECTED:
        fail(f"domain counts differ: {dict(domains)}")
    maturity = Counter(pattern["maturity"] for pattern in patterns)
    if maturity != Counter({"reference": 25, "candidate": 40, "catalog": 135}):
        fail(f"maturity counts differ: {dict(maturity)}")
    references = {pattern["id"] for pattern in patterns if pattern["maturity"] == "reference"}
    if references != REFERENCE_IDS:
        fail("v1.0 reference ID set changed")
    executable = list((ROOT / "benchmarks/executable").rglob("*.json"))
    scaffolds = list((ROOT / "benchmarks/scaffolds").rglob("*.json"))
    pages = list((ROOT / "patterns").rglob("CAAP-*.md"))
    counts = (len(executable), len(scaffolds), len(pages))
    if counts != (25, 175, 200):
        fail(
            "artifact counts differ: "
            f"executable={counts[0]}, scaffolds={counts[1]}, pages={counts[2]}"
        )
    for path in executable + scaffolds:
        case = json.loads(path.read_text())
        if not all(case["safety"].values()):
            fail(f"unsafe or incomplete safety declaration: {path}")
        if case["pattern_id"] not in ids:
            fail(f"unknown pattern ID in {path}")
    for pattern in patterns:
        for relation_type, related in pattern["relationships"].items():
            unknown = set(related) - set(ids)
            if unknown:
                fail(f"unknown {relation_type} relation in {pattern['id']}: {sorted(unknown)}")
    check_definitions_and_severity(patterns)
    assessments = check_assessment_cases(patterns)
    check_package_data(executable, assessments)
    check_schemas(registry, executable + scaffolds, assessments)
    check_versions()
    print(
        "Repository invariants validated: 200 patterns, 25 executable cases, 175 scaffolds, "
        "200 assessment cases."
    )


LAYERS = ("adversarial", "cortical", "governance", "recovery")


def check_assessment_cases(patterns: list[dict]) -> list[Path]:
    """One paired-trial assessment case per pattern, with layer and sentinel consistency."""
    paths = sorted((ROOT / "assessments/cases").rglob("*.json"))
    if len(paths) != 200:
        fail(f"expected 200 assessment cases, found {len(paths)}")
    by_id = {pattern["id"]: pattern for pattern in patterns}
    if {pattern["integrity_layer"] for pattern in patterns} - set(LAYERS):
        fail("pattern integrity_layer outside the four layers")
    trials = 0
    for path in paths:
        case = json.loads(path.read_text())
        pattern = by_id.get(case["pattern_id"])
        if pattern is None:
            fail(f"assessment case {path.name} references an unknown pattern")
        if case["integrity_layer"] != pattern["integrity_layer"]:
            fail(f"{case['id']}: layer differs from the registry")
        if case["required_capabilities"] != pattern["required_capabilities"]:
            fail(f"{case['id']}: capabilities differ from the registry")
        if not all(case["safety"].values()):
            fail(f"unsafe or incomplete safety declaration: {path}")
        kinds = [trial["kind"] for trial in case["trials"]]
        if kinds != ["benign_control", "adversarial_condition"]:
            fail(f"{case['id']}: trials must be a benign control then an adversarial condition")
        adversarial = case["trials"][1]
        content = adversarial["untrusted_content"]
        if case["safe_sentinel"] not in content or "CAAP TEST ONLY" not in content:
            fail(
                f"{case['id']}: untrusted content must carry the sentinel "
                "and the CAAP TEST ONLY label"
            )
        sinks = re.findall(r"\b\w+_sink\b", content)
        if any(not sink.startswith("mock_") for sink in sinks):
            fail(f"{case['id']}: untrusted content may name only mock sinks: {sinks}")
        if re.search(r"\b\w+://", content):
            fail(f"{case['id']}: untrusted content must not carry a URL")
        trials += len(case["trials"])
    if trials != 400:
        fail(f"expected 400 assessment trials, found {trials}")
    return paths


SEVERITY_AXES = ("impact", "exploitability", "privilege", "autonomy", "persistence", "propagation")
SEVERITY_WEIGHTS = (2, 2, 1, 1, 1, 1)


def severity_from_vector(vector: dict) -> float:
    pairs = zip(SEVERITY_WEIGHTS, SEVERITY_AXES, strict=True)
    weighted = sum(w * vector[axis] for w, axis in pairs)
    return round(10 * weighted / (5 * sum(SEVERITY_WEIGHTS)), 1)


def expected_rating(score: float) -> str:
    if score >= 9.0:
        return "critical"
    if score >= 7.0:
        return "high"
    return "medium" if score >= 4.0 else "low"


def check_definitions_and_severity(patterns: list[dict]) -> None:
    """Definitions are pattern-specific; severity vectors and scores follow docs/STANDARD.md."""
    definitions = [pattern["definition"] for pattern in patterns]
    if len(set(definitions)) != len(definitions):
        fail("pattern definitions are not unique")
    for pattern in patterns:
        if pattern["definition"].startswith("Tests whether"):
            fail(f"{pattern['id']} still carries the template definition")
        severity = pattern["severity"]
        vector = severity["vector"]
        if set(vector) != set(SEVERITY_AXES) or any(not 1 <= vector[a] <= 5 for a in SEVERITY_AXES):
            fail(f"{pattern['id']}: severity vector must score each of the six axes 1..5")
        score, derived = severity["baseline_score"], severity_from_vector(vector)
        if severity["rating"] != expected_rating(score):
            fail(f"{pattern['id']}: rating {severity['rating']} does not match score {score}")
        if pattern["maturity"] == "reference":
            if severity["score_source"] != "caap-v1.0-baseline" or abs(score - derived) > 0.5:
                fail(
                    f"{pattern['id']}: reference score {score} must be the v1.0 baseline "
                    f"within 0.5 of the vector-derived {derived}"
                )
        elif severity["score_source"] != "vector-derived" or score != derived:
            fail(f"{pattern['id']}: score {score} does not equal the vector-derived {derived}")


def check_schemas(registry: dict, cases: list[Path], assessments: list[Path]) -> None:
    """Validate the registry and every case against the published JSON Schemas."""
    registry_errors = schema_errors("taxonomy", registry)
    if registry_errors is None:
        print("NOTE: jsonschema is not installed; skipping full JSON Schema validation.")
        return
    if registry_errors:
        fail("taxonomy schema violations: " + "; ".join(registry_errors[:5]))
    for path in cases:
        errors = schema_errors("test-case", json.loads(path.read_text()))
        if errors:
            detail = "; ".join(errors[:5])
            fail(f"test-case schema violations in {path.relative_to(ROOT)}: {detail}")
    for path in assessments:
        errors = schema_errors("agent-assessment-case", json.loads(path.read_text()))
        if errors:
            detail = "; ".join(errors[:5])
            fail(f"assessment-case schema violations in {path.relative_to(ROOT)}: {detail}")
    print(
        f"JSON Schema validation passed: registry, {len(cases)} cases, "
        f"{len(assessments)} assessment cases."
    )


def check_package_data(executable: list[Path], assessments: list[Path]) -> None:
    """The copies bundled into the wheel must mirror the canonical files exactly."""
    expected = {ROOT / "data/taxonomy/caap-200.json": PACKAGE_DATA / "taxonomy/caap-200.json"}
    for source in sorted((ROOT / "schemas").glob("*.schema.json")):
        expected[source] = PACKAGE_DATA / "schemas" / source.name
    for source in sorted((ROOT / "profiles").glob("*.json")):
        expected[source] = PACKAGE_DATA / "profiles" / source.name
    for source in assessments:
        expected[source] = PACKAGE_DATA / "assessments" / source.relative_to(ROOT / "assessments")
    for source in executable:
        relative = source.relative_to(ROOT / "benchmarks")
        expected[source] = PACKAGE_DATA / "benchmarks" / relative
    for source, packaged in expected.items():
        if not packaged.is_file():
            fail(f"missing packaged copy: {packaged.relative_to(ROOT)}")
        if packaged.read_bytes() != source.read_bytes():
            fail(f"packaged copy differs from {source.relative_to(ROOT)}")
    extra = {path for path in PACKAGE_DATA.rglob("*") if path.is_file()} - set(expected.values())
    if extra:
        fail(f"unexpected packaged files: {sorted(str(p.relative_to(ROOT)) for p in extra)}")


def check_versions() -> None:
    """pyproject.toml, versions.py, the README, and the changelog must agree on the version."""
    import release  # noqa: PLC0415

    pyproject = release._match(release.PYPROJECT_RE, (ROOT / "pyproject.toml").read_text(), "p")
    problems = [
        problem
        for problem in release.check(pyproject, ROOT)
        if not problem.startswith("CHANGELOG.md has no `## [")
        and not problem.startswith("CHANGELOG.md still has entries under [Unreleased]")
    ]
    if problems:
        fail("version drift: " + "; ".join(problems))
    if "## [Unreleased]" not in (ROOT / "CHANGELOG.md").read_text():
        fail("CHANGELOG.md has no [Unreleased] section")
    print(f"Version {pyproject} is consistent across pyproject.toml, versions.py, and README.md.")


if __name__ == "__main__":
    main()
