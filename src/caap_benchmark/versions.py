"""Version identifiers shared by reports, assessments, evidence bundles, and the CLI.

`PACKAGE_VERSION` must equal the version in pyproject.toml; `scripts/release.py check`
and repository validation enforce that. `TAXONOMY_VERSION` is the CAAP-200 working
taxonomy version and changes independently of the software.
"""

from __future__ import annotations

from importlib import metadata

PACKAGE_VERSION = "0.1.0"
TAXONOMY_VERSION = "2.0.0-draft.1"


def package_version() -> str:
    """The installed distribution version, or the source version when not installed."""
    try:
        return metadata.version("caap-benchmark")
    except metadata.PackageNotFoundError:
        return PACKAGE_VERSION
