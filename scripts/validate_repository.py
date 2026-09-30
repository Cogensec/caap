#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_DATA = ROOT / "src" / "caap_benchmark" / "data"
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
    check_package_data(executable)
    print("Repository invariants validated: 200 patterns, 25 executable cases, 175 scaffolds.")


def check_package_data(executable: list[Path]) -> None:
    """The copies bundled into the wheel must mirror the canonical files exactly."""
    expected = {ROOT / "data/taxonomy/caap-200.json": PACKAGE_DATA / "taxonomy/caap-200.json"}
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


if __name__ == "__main__":
    main()
