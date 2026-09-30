from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .schemas import load_schema, schema_errors


class ValidationError(ValueError):
    pass


def load_data(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    if source.suffix.lower() == ".json":
        value = json.loads(source.read_text(encoding="utf-8"))
    elif source.suffix.lower() in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore[import-not-found]
        except ImportError as exc:
            raise RuntimeError("YAML input requires: pip install 'caap-benchmark[yaml]'") from exc
        value = yaml.safe_load(source.read_text(encoding="utf-8"))
    else:
        raise ValidationError(f"Unsupported file type: {source.suffix}")
    if not isinstance(value, dict):
        raise ValidationError(f"Expected an object at the root of {source}")
    return value


def discover_tests(paths: list[str | Path]) -> list[Path]:
    found: set[Path] = set()
    for raw in paths:
        path = Path(raw)
        if path.is_file() and path.suffix.lower() in {".json", ".yaml", ".yml"}:
            found.add(path.resolve())
        elif path.is_dir():
            for suffix in ("*.json", "*.yaml", "*.yml"):
                found.update(item.resolve() for item in path.rglob(suffix))
    return sorted(found)


def validate_test_case(case: dict[str, Any]) -> list[str]:
    """Validate a case against the published test-case schema.

    Uses full JSON Schema validation when `jsonschema` is installed and the
    structural check below otherwise. Either way an empty list means valid.
    """
    errors = schema_errors("test-case", case)
    if errors is None:
        errors = structural_test_case_errors(case)
    return errors


def structural_test_case_errors(case: dict[str, Any]) -> list[str]:
    """Dependency-free subset of the schema: required fields, ID shape, oracles, safety."""
    schema = load_schema("test-case")
    errors: list[str] = []
    missing = sorted(set(schema["required"]) - case.keys())
    if missing:
        errors.append("missing required fields: " + ", ".join(missing))
    id_pattern = schema["properties"]["pattern_id"]["pattern"]
    if not re.fullmatch(id_pattern, str(case.get("pattern_id", ""))):
        errors.append(f"pattern_id must match {id_pattern}")
    if not isinstance(case.get("procedure", []), list) or not case.get("procedure"):
        errors.append("procedure must be a non-empty list")
    for field_name in ("success_oracles", "secure_behavior_oracles"):
        if not isinstance(case.get(field_name, []), list) or not case.get(field_name):
            errors.append(f"{field_name} must be a non-empty list")
    safety = case.get("safety", {})
    if isinstance(safety, dict):
        for key in schema["$defs"]["safety"]["required"]:
            if safety.get(key) is not True:
                errors.append(f"safety.{key} must be true")
    else:
        errors.append("safety must be an object")
    return errors
