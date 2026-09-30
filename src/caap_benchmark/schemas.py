"""Access to the published CAAP JSON Schemas and validation against them.

Full JSON Schema validation uses the optional `jsonschema` package
(`pip install 'caap-benchmark[schema]'`). Without it, callers fall back to a
structural check that derives its required-field list from the same schema, so
the two can never disagree about which fields a record must carry.
"""

from __future__ import annotations

import json
from functools import cache
from importlib import resources
from typing import Any

SCHEMA_NAMES: tuple[str, ...] = (
    "taxonomy",
    "test-case",
    "adapter-response",
    "report",
    "agent-assessment-case",
    "agent-assessment-response",
    "agent-assessment-manifest",
    "agent-assessment-report",
    "evidence-bundle",
)


@cache
def load_schema(name: str) -> dict[str, Any]:
    """Return the bundled schema by short name, for example "test-case"."""
    if name not in SCHEMA_NAMES:
        raise ValueError(f"unknown schema: {name}; expected one of {', '.join(SCHEMA_NAMES)}")
    path = resources.files("caap_benchmark") / "data" / "schemas" / f"{name}.schema.json"
    return json.loads(path.read_text(encoding="utf-8"))


def jsonschema_available() -> bool:
    try:
        import jsonschema  # noqa: F401
    except ImportError:
        return False
    return True


def validator_name() -> str:
    """Human-readable name of the validator in use, for CLI output."""
    if jsonschema_available():
        return "jsonschema"
    return "structural (install 'caap-benchmark[schema]' for full JSON Schema validation)"


@cache
def _validator(name: str) -> Any:
    import jsonschema

    return jsonschema.Draft202012Validator(load_schema(name))


def schema_errors(name: str, instance: Any) -> list[str] | None:
    """Return JSON Schema violations, or None when `jsonschema` is not installed."""
    if not jsonschema_available():
        return None
    errors = sorted(_validator(name).iter_errors(instance), key=lambda e: [str(p) for p in e.path])
    return [f"{_location(error)}: {error.message}" for error in errors]


def _location(error: Any) -> str:
    path = "/".join(str(part) for part in error.absolute_path)
    return path or "$"
