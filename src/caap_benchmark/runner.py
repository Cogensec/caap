from __future__ import annotations

import hashlib
import json
import time
from datetime import datetime, timezone
from typing import Any

from .adapters.base import AgentAdapter
from .loaders import ValidationError, validate_test_case
from .models import ResultState, RunResult
from .oracles import matched_oracles


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


class BenchmarkRunner:
    def __init__(self, adapter: AgentAdapter):
        self.adapter = adapter

    def run(self, case: dict[str, Any]) -> RunResult:
        errors = validate_test_case(case)
        if errors:
            raise ValidationError("; ".join(errors))
        started_at = _now()
        start = time.monotonic()
        response = self.adapter.execute(case)
        finished_at = _now()
        duration_ms = round((time.monotonic() - start) * 1000)
        missing = [key for key in case["telemetry_required"] if key not in response.telemetry]
        attack_matched: list[str] = []
        secure_matched: list[str] = []

        if response.error:
            state = ResultState.TEST_ERROR
        elif not response.applicable:
            state = ResultState.NOT_APPLICABLE
        elif missing:
            state = ResultState.INCONCLUSIVE
        else:
            attack_matched = matched_oracles(case["success_oracles"], response)
            secure_matched = matched_oracles(case["secure_behavior_oracles"], response)
            required_secure = {str(value["id"]) for value in case["secure_behavior_oracles"]}
            if attack_matched:
                state = ResultState.FAIL
            elif required_secure.issubset(secure_matched):
                state = ResultState.PASS
            else:
                state = ResultState.INCONCLUSIVE

        evidence_payload = {
            "test_id": case["id"],
            "pattern_id": case["pattern_id"],
            "adapter": self.adapter.name,
            "events": [{"type": event.type, "data": event.data} for event in response.events],
            "telemetry": response.telemetry,
            "response": response.response,
        }
        canonical = json.dumps(evidence_payload, sort_keys=True, separators=(",", ":"))
        evidence_payload["sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        recovery = case.get("recovery", {})
        recovery_status = "required" if state == ResultState.FAIL else str(
            recovery.get("status_on_secure_result", "not_required")
        )
        return RunResult(
            test_id=str(case["id"]),
            pattern_id=str(case["pattern_id"]),
            title=str(case["title"]),
            state=state,
            severity=float(case["severity"]["baseline_score"]),
            started_at=started_at,
            finished_at=finished_at,
            duration_ms=duration_ms,
            adapter=self.adapter.name,
            attack_oracles_matched=attack_matched,
            secure_oracles_matched=secure_matched,
            missing_telemetry=missing,
            recovery_status=recovery_status,
            evidence=evidence_payload,
            error=response.error,
        )

