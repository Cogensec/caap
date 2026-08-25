from __future__ import annotations

import json
from pathlib import Path
from typing import Any


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
    errors: list[str] = []
    required = {
        "schema_version",
        "id",
        "pattern_id",
        "title",
        "authorization",
        "benign_objective",
        "adversarial_condition",
        "safe_sentinel",
        "procedure",
        "success_oracles",
        "secure_behavior_oracles",
        "telemetry_required",
        "severity",
        "mappings",
        "recovery",
        "safety",
    }
    missing = sorted(required - case.keys())
    if missing:
        errors.append("missing required fields: " + ", ".join(missing))
    if not str(case.get("pattern_id", "")).startswith("CAAP-"):
        errors.append("pattern_id must start with CAAP-")
    if not isinstance(case.get("procedure", []), list) or not case.get("procedure"):
        errors.append("procedure must be a non-empty list")
    for field_name in ("success_oracles", "secure_behavior_oracles"):
        if not isinstance(case.get(field_name, []), list) or not case.get(field_name):
            errors.append(f"{field_name} must be a non-empty list")
    safety = case.get("safety", {})
    if isinstance(safety, dict):
        for key in (
            "authorized_targets_only",
            "synthetic_data_only",
            "mock_tools_only",
            "no_destructive_payloads",
            "no_real_exfiltration",
            "no_persistence",
        ):
            if safety.get(key) is not True:
                errors.append(f"safety.{key} must be true")
    else:
        errors.append("safety must be an object")
    return errors

