from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class ResultState(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    INCONCLUSIVE = "inconclusive"
    TEST_ERROR = "test_error"
    NOT_APPLICABLE = "not_applicable"


@dataclass(frozen=True)
class Event:
    type: str
    data: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> Event:
        return cls(type=str(value["type"]), data=dict(value.get("data", {})))


@dataclass
class AdapterResponse:
    events: list[Event]
    response: str = ""
    telemetry: dict[str, Any] = field(default_factory=dict)
    applicable: bool = True
    error: str | None = None


@dataclass
class RunResult:
    test_id: str
    pattern_id: str
    title: str
    state: ResultState
    severity: float
    started_at: str
    finished_at: str
    duration_ms: int
    adapter: str
    attack_oracles_matched: list[str] = field(default_factory=list)
    secure_oracles_matched: list[str] = field(default_factory=list)
    missing_telemetry: list[str] = field(default_factory=list)
    recovery_status: str = "not_required"
    evidence: dict[str, Any] = field(default_factory=dict)
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["state"] = self.state.value
        return value


@dataclass
class Scorecard:
    total: int
    passed: int
    failed: int
    inconclusive: int
    test_errors: int
    not_applicable: int
    security_score: float | None
    severity_weighted_score: float | None
    coverage_percent: float

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

