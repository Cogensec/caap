#!/usr/bin/env python3
"""Release helper: bump the version, check release readiness, extract release notes.

    python3 scripts/release.py bump 0.2.0      # move Unreleased into 0.2.0, set versions
    python3 scripts/release.py check 0.2.0     # verify the tree is ready to tag v0.2.0
    python3 scripts/release.py notes 0.2.0     # print the release notes for the tag

The process is documented in docs/RELEASING.md. The release workflow runs `check`
against the pushed tag and `notes` to build the GitHub release body.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.]+)?$")
HEADING_RE = re.compile(r"^## \[(?P<name>[^\]]+)\](?: - (?P<date>\d{4}-\d{2}-\d{2}))?\s*$")
PYPROJECT_RE = re.compile(r'^version = "(?P<version>[^"]+)"$', re.MULTILINE)
PACKAGE_RE = re.compile(r'^PACKAGE_VERSION = "(?P<version>[^"]+)"$', re.MULTILINE)
TAXONOMY_RE = re.compile(r'^TAXONOMY_VERSION = "(?P<version>[^"]+)"$', re.MULTILINE)
README_RE = re.compile(r"`v(?P<version>[^`]+)` software")
UNRELEASED_PLACEHOLDER = "_No unreleased changes yet._"


class ReleaseError(Exception):
    pass


def _paths(root: Path) -> dict[str, Path]:
    return {
        "pyproject": root / "pyproject.toml",
        "versions": root / "src/caap_benchmark/versions.py",
        "changelog": root / "CHANGELOG.md",
        "readme": root / "README.md",
    }


def _match(pattern: re.Pattern[str], text: str, label: str) -> str:
    found = pattern.search(text)
    if not found:
        raise ReleaseError(f"could not find the version in {label}")
    return found.group("version")


def changelog_sections(text: str) -> list[tuple[str, str | None, str]]:
    """Return (name, date, body) for every `## [name]` section in order."""
    sections: list[tuple[str, str | None, list[str]]] = []
    for line in text.splitlines():
        heading = HEADING_RE.match(line)
        if heading:
            sections.append((heading.group("name"), heading.group("date"), []))
        elif sections:
            sections[-1][2].append(line)
    return [(name, when, "\n".join(body).strip()) for name, when, body in sections]


def _section(text: str, name: str) -> tuple[str | None, str] | None:
    for section_name, when, body in changelog_sections(text):
        if section_name == name:
            return when, body
    return None


def _has_entries(body: str) -> bool:
    return any(line.startswith(("- ", "* ")) for line in body.splitlines())


def check(version: str, root: Path = ROOT, tag: str | None = None) -> list[str]:
    """Return a list of problems; an empty list means the tree is ready to tag."""
    problems: list[str] = []
    if not VERSION_RE.match(version):
        return [f"{version!r} is not a release version (expected MAJOR.MINOR.PATCH[-pre])"]
    if tag is not None and tag != f"v{version}":
        problems.append(f"tag {tag} does not match version {version} (expected v{version})")
    paths = _paths(root)
    try:
        pyproject = _match(PYPROJECT_RE, paths["pyproject"].read_text(), "pyproject.toml")
        package = _match(PACKAGE_RE, paths["versions"].read_text(), "versions.py")
        readme = _match(README_RE, paths["readme"].read_text(), "README.md status")
    except (OSError, ReleaseError) as exc:
        return problems + [str(exc)]
    located = (("pyproject.toml", pyproject), ("versions.py", package), ("README.md", readme))
    for label, found in located:
        if found != version:
            problems.append(f"{label} says {found}, expected {version}")
    changelog = paths["changelog"].read_text()
    section = _section(changelog, version)
    if section is None:
        problems.append(f"CHANGELOG.md has no `## [{version}] - YYYY-MM-DD` section")
    else:
        when, body = section
        if when is None:
            problems.append(f"CHANGELOG.md section [{version}] has no release date")
        if not _has_entries(body):
            problems.append(f"CHANGELOG.md section [{version}] has no entries")
    unreleased = _section(changelog, "Unreleased")
    if unreleased is not None and _has_entries(unreleased[1]):
        problems.append(
            "CHANGELOG.md still has entries under [Unreleased]; move them into the release"
        )
    sections = changelog_sections(changelog)
    names = [name for name, _, _ in sections]
    if names and names[0] != "Unreleased" and names[0] != version:
        problems.append(
            f"CHANGELOG.md's first section is [{names[0]}], "
            f"expected [Unreleased] or [{version}]"
        )
    return problems


def notes(version: str, root: Path = ROOT) -> str:
    """Render the GitHub release body for a version from the changelog."""
    paths = _paths(root)
    section = _section(paths["changelog"].read_text(), version)
    if section is None:
        raise ReleaseError(f"CHANGELOG.md has no section for {version}")
    when, body = section
    taxonomy = _match(TAXONOMY_RE, paths["versions"].read_text(), "versions.py")
    header = f"caap-benchmark {version}"
    if when:
        header += f" ({when})"
    lines = [
        f"**{header}** implementing the CAAP-200 working taxonomy `{taxonomy}`.",
        "",
        body,
        "",
        "Assets: the wheel and source distribution, the canonical taxonomy JSON and YAML, "
        "the JSON Schemas, and `SHA256SUMS` over all of them. Install with "
        f"`python -m pip install caap_benchmark-{version.replace('-', '')}-py3-none-any.whl` "
        "or run from a checkout with `PYTHONPATH=src python3 -m caap_benchmark.cli`.",
    ]
    return "\n".join(lines).rstrip() + "\n"


def bump(version: str, root: Path = ROOT, today: date | None = None) -> list[str]:
    """Set every version location to `version` and cut the changelog. Returns changed paths."""
    if not VERSION_RE.match(version):
        raise ReleaseError(
            f"{version!r} is not a release version (expected MAJOR.MINOR.PATCH[-pre])"
        )
    paths = _paths(root)
    when = (today or date.today()).isoformat()
    changed = []
    pyproject = paths["pyproject"].read_text()
    current = _match(PYPROJECT_RE, pyproject, "pyproject.toml")
    if current == version:
        raise ReleaseError(f"pyproject.toml is already at {version}")
    paths["pyproject"].write_text(PYPROJECT_RE.sub(f'version = "{version}"', pyproject, count=1))
    changed.append(paths["pyproject"])
    versions = paths["versions"].read_text()
    _match(PACKAGE_RE, versions, "versions.py")
    paths["versions"].write_text(
        PACKAGE_RE.sub(f'PACKAGE_VERSION = "{version}"', versions, count=1)
    )
    changed.append(paths["versions"])
    readme = paths["readme"].read_text()
    _match(README_RE, readme, "README.md status")
    paths["readme"].write_text(README_RE.sub(f"`v{version}` software", readme, count=1))
    changed.append(paths["readme"])
    changelog = paths["changelog"].read_text()
    unreleased = _section(changelog, "Unreleased")
    if unreleased is None:
        raise ReleaseError("CHANGELOG.md has no [Unreleased] section to cut")
    if not _has_entries(unreleased[1]):
        raise ReleaseError("CHANGELOG.md has nothing under [Unreleased] to release")
    if _section(changelog, version) is not None:
        raise ReleaseError(f"CHANGELOG.md already has a [{version}] section")
    replacement = f"## [Unreleased]\n\n{UNRELEASED_PLACEHOLDER}\n\n## [{version}] - {when}"
    changelog = re.sub(
        r"^## \[Unreleased\][ \t]*$", replacement, changelog, count=1, flags=re.MULTILINE
    )
    paths["changelog"].write_text(changelog)
    changed.append(paths["changelog"])
    return [str(path.relative_to(root)) for path in changed]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)
    sub = parser.add_subparsers(dest="command", required=True)
    cmd_bump = sub.add_parser("bump", help="set the version everywhere and cut the changelog")
    cmd_bump.add_argument("version")
    cmd_check = sub.add_parser("check", help="verify the tree is ready to tag this version")
    cmd_check.add_argument("version")
    cmd_check.add_argument("--tag", help="the git tag being released; must equal v<version>")
    cmd_notes = sub.add_parser("notes", help="print the release notes for a version")
    cmd_notes.add_argument("version")
    args = parser.parse_args(argv)
    root = Path(args.root)
    try:
        if args.command == "bump":
            for path in bump(args.version, root):
                print(f"updated {path}")
            print(f"Review CHANGELOG.md, then commit as 'chore: release {args.version}'.")
            return 0
        if args.command == "check":
            problems = check(args.version, root, args.tag)
            for problem in problems:
                print(f"ERROR: {problem}", file=sys.stderr)
            if not problems:
                print(f"Ready to release {args.version}.")
            return 1 if problems else 0
        sys.stdout.write(notes(args.version, root))
        return 0
    except (OSError, ReleaseError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
