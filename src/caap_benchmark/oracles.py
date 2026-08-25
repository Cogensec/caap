from __future__ import annotations

from typing import Any

from .models import AdapterResponse, Event


def _matches(event: Event, oracle: dict[str, Any]) -> bool:
    if event.type != oracle.get("event_type"):
        return False
    where = oracle.get("where", {})
    if not isinstance(where, dict):
        return False
    for key, expected in where.items():
        actual = event.data.get(key)
        if isinstance(expected, dict) and "contains" in expected:
            if str(expected["contains"]) not in str(actual):
                return False
        elif actual != expected:
            return False
    return True


def evaluate_oracle(oracle: dict[str, Any], response: AdapterResponse) -> bool:
    oracle_type = oracle.get("type")
    if oracle_type == "event_present":
        return any(_matches(event, oracle) for event in response.events)
    if oracle_type == "event_absent":
        return not any(_matches(event, oracle) for event in response.events)
    if oracle_type == "response_contains":
        return str(oracle.get("value", "")) in response.response
    if oracle_type == "response_excludes":
        return str(oracle.get("value", "")) not in response.response
    if oracle_type == "telemetry_equals":
        return response.telemetry.get(oracle.get("key")) == oracle.get("value")
    raise ValueError(f"Unknown oracle type: {oracle_type}")


def matched_oracles(oracles: list[dict[str, Any]], response: AdapterResponse) -> list[str]:
    matched: list[str] = []
    for oracle in oracles:
        if evaluate_oracle(oracle, response):
            matched.append(str(oracle.get("id", "unnamed-oracle")))
    return matched

