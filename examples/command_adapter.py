#!/usr/bin/env python3
"""Minimal safe command-adapter contract example; reads one case from stdin.

This example replays the case's declared secure trace so the contract can be
exercised end to end. A real adapter MUST derive events from the target's own
trace; replaying the declared trace proves nothing about an agent.
"""

from __future__ import annotations

import json
import sys

from caap_benchmark.events import telemetry_from_events

request = json.load(sys.stdin)
case = request["caap_test"]
trace = case.get("mock_scenario", {}).get("safe")
if trace:
    events = trace["events"]
    response = trace["response"]
else:
    events = [
        {"type": "message_received", "data": {"trust": "untrusted"}},
        {"type": "plan_created", "data": {"objective": case["benign_objective"]}},
        {
            "type": "policy_decision",
            "data": {"decision": "deny", "reason": "untrusted instruction"},
        },
    ]
    response = "Synthetic fixture rejected; approved objective retained."
output = {
    "response": response,
    "events": events,
    "telemetry": telemetry_from_events(events),
    "applicable": True,
}
json.dump(output, sys.stdout)
