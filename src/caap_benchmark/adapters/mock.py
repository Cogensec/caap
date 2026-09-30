from __future__ import annotations

from typing import Any

from ..events import telemetry_from_events
from ..models import AdapterResponse, Event
from ..safety import SyntheticSink
from .base import AgentAdapter


class MockAdapter(AgentAdapter):
    """Deterministic safe/vulnerable agent used for validation and examples.

    A case that carries a `mock_scenario` declares the exact secure and vulnerable
    event traces for its mechanism; the mock replays the selected trace. In the
    vulnerable mode it additionally records the case sentinel through the synthetic
    sink, which is the only side effect the mock can produce. A case without a
    scenario, such as a contributor scaffold, gets a generic trace.
    """

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
        scenario = test_case.get("mock_scenario")
        if isinstance(scenario, dict):
            trace = scenario["vulnerable" if self.vulnerable else "safe"]
            events = [Event.from_dict(value) for value in trace["events"]]
            response = str(trace["response"])
            if self.vulnerable:
                events.append(Event("sentinel_reached", SyntheticSink().record(sentinel)))
        else:
            events, response = self._generic_trace(test_case, sentinel)
        return AdapterResponse(
            events=events, response=response, telemetry=telemetry_from_events(events)
        )

    def _generic_trace(self, test_case: dict[str, Any], sentinel: str) -> tuple[list[Event], str]:
        carrier = str(test_case.get("attack_fixture", {}).get("carrier", "synthetic-content"))
        events = [
            Event("message_received", {"trust": "untrusted", "carrier": carrier}),
            Event("plan_created", {"objective": str(test_case["benign_objective"])}),
        ]
        if self.vulnerable:
            events.append(
                Event("policy_decision", {"decision": "allow", "reason": "unsafe simulated path"})
            )
            events.append(Event("sentinel_reached", SyntheticSink().record(sentinel)))
            return events, f"Simulated unsafe path reached {sentinel}."
        events.append(
            Event("policy_decision", {"decision": "deny", "reason": "untrusted instruction"})
        )
        events.append(Event("safe_objective_completed", {"synthetic": True}))
        return events, "The untrusted request was rejected; the benign objective completed safely."
