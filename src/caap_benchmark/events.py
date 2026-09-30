"""Event vocabulary shared by the generator, the mock adapter, and adapter examples.

Adapters normalize a target's trace into events. Each event type maps to one
telemetry key so a case can require the telemetry that its oracles inspect and
a runner can report `inconclusive` when that telemetry is missing.
"""

from __future__ import annotations

from typing import Any

BASE_TELEMETRY_KEYS: tuple[str, ...] = (
    "messages",
    "plans",
    "tool_calls",
    "policy_decisions",
    "events",
)

TELEMETRY_KEY_BY_EVENT: dict[str, str] = {
    # Conversation and planning
    "message_received": "messages",
    "plan_created": "plans",
    "plan_updated": "plans",
    "objective_preserved": "plans",
    "plan_step_dispatched": "plans",
    "plan_step_rejected": "plans",
    "policy_decision": "policy_decisions",
    # Instruction handling
    "instruction_classified": "instruction_events",
    "scheduled_trigger": "instruction_events",
    "template_instruction": "instruction_events",
    "server_response": "instruction_events",
    "summary_produced": "instruction_events",
    "description_produced": "instruction_events",
    "reminder_processed": "instruction_events",
    "answer_produced": "instruction_events",
    # Tools
    "tool_call": "tool_calls",
    "tool_selected": "tool_events",
    "tool_result": "tool_events",
    "budget_enforced": "tool_events",
    "data_flow_blocked": "tool_events",
    # Memory and retrieval
    "memory_write": "memory_events",
    "memory_write_rejected": "memory_events",
    "memory_read": "memory_events",
    "memory_activated": "memory_events",
    "memory_quarantined": "memory_events",
    "retrieval": "retrievals",
    # Identity, authorization, and revocation
    "delegation": "identity_events",
    "scope_check": "identity_events",
    "credential_use": "identity_events",
    "authorization_check": "identity_events",
    "access_request_drafted": "identity_events",
    "capability_used": "identity_events",
    "use_time_check": "identity_events",
    "revocation": "identity_events",
    # Components and code
    "component_loaded": "component_events",
    "code_execution": "code_executions",
    "argument_escaped": "code_executions",
    "path_check": "code_executions",
    # Agents, approvals, autonomy, actuation
    "agent_message": "agent_messages",
    "approval_request": "approvals",
    "approval_granted": "approvals",
    "task_created": "autonomy_events",
    "agent_halted": "autonomy_events",
    "actuator_command": "actuator_commands",
    # Outcomes
    "sentinel_reached": "sink_events",
    "safe_objective_completed": "outcomes",
}

ALL_TELEMETRY_KEYS: tuple[str, ...] = tuple(
    sorted(set(BASE_TELEMETRY_KEYS) | set(TELEMETRY_KEY_BY_EVENT.values()))
)


def telemetry_from_events(events: list[Any]) -> dict[str, Any]:
    """Group events into telemetry keys; every known key is present even when empty.

    Accepts `Event` objects or `{"type": ..., "data": {...}}` dicts so adapter examples
    can reuse it without depending on the models module.
    """
    telemetry: dict[str, Any] = {key: [] for key in ALL_TELEMETRY_KEYS}
    types: list[str] = []
    for event in events:
        if isinstance(event, dict):
            event_type, data = str(event["type"]), dict(event.get("data", {}))
        else:
            event_type, data = event.type, dict(event.data)
        types.append(event_type)
        telemetry.setdefault(TELEMETRY_KEY_BY_EVENT.get(event_type, "other_events"), []).append(
            data
        )
    telemetry["events"] = types
    return telemetry
