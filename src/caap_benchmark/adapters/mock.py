from __future__ import annotations

from typing import Any

from ..models import AdapterResponse, Event
from ..safety import SyntheticSink
from .base import AgentAdapter


class MockAdapter(AgentAdapter):
    """Deterministic safe/vulnerable agent used for validation and examples."""

    name = "mock"

    def __init__(self, vulnerable: bool = False) -> None:
        self.vulnerable = vulnerable

    def execute(self, test_case: dict[str, Any]) -> AdapterResponse:
        required = set(test_case.get("required_capabilities", []))
        available = set(test_case.get("mock_target", {}).get("capabilities", required))
        if not required.issubset(available):
            return AdapterResponse(
                events=[],
                telemetry={"messages": [], "policy_decisions": []},
                applicable=False,
            )

        sentinel = str(test_case["safe_sentinel"])
        carrier = str(test_case.get("attack_fixture", {}).get("carrier", "synthetic-content"))
        events = [
            Event("message_received", {"trust": "untrusted", "carrier": carrier}),
            Event("plan_created", {"objective": str(test_case["benign_objective"])}),
        ]
        if self.vulnerable:
            sink_result = SyntheticSink().record(sentinel)
            events.extend(
                [
                    Event(
                        "policy_decision",
                        {"decision": "allow", "reason": "unsafe simulated path"},
                    ),
                    Event(
                        "sentinel_reached",
                        sink_result,
                    ),
                ]
            )
            response = f"Simulated unsafe path reached {sentinel}."
        else:
            events.extend(
                [
                    Event(
                        "policy_decision",
                        {"decision": "deny", "reason": "untrusted instruction"},
                    ),
                    Event("safe_objective_completed", {"synthetic": True}),
                ]
            )
            response = "The untrusted request was rejected; the benign objective completed safely."

        telemetry = {
            "messages": [event.data for event in events if event.type == "message_received"],
            "plans": [event.data for event in events if event.type == "plan_created"],
            "tool_calls": [event.data for event in events if event.type == "sentinel_reached"],
            "policy_decisions": [
                event.data for event in events if event.type == "policy_decision"
            ],
            "events": [event.type for event in events],
        }
        return AdapterResponse(events=events, response=response, telemetry=telemetry)
