"""Version identifiers shared by reports, assessments, and evidence bundles."""

from __future__ import annotations

from importlib import metadata

TAXONOMY_VERSION = "2.0.0-draft.1"


def package_version() -> str:
    try:
        return metadata.version("caap-benchmark")
    except metadata.PackageNotFoundError:
        return "0.1.0"
