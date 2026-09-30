#!/usr/bin/env python3
"""Minimal safe command-adapter contract example; reads one case from stdin."""

from __future__ import annotations

import json
import sys

request = json.load(sys.stdin)
case = request["caap_test"]
output = {
    "response": "Synthetic fixture rejected; approved objective retained.",
    "events": [
        {"type": "message_received", "data": {"trust": "untrusted"}},
        {"type": "plan_created", "data": {"objective": case["benign_objective"]}},
        {
            "type": "policy_decision",
            "data": {"decision": "deny", "reason": "untrusted instruction"},
        },
    ],
    "telemetry": {
        "messages": [{"trust": "untrusted"}],
        "plans": [{"objective": case["benign_objective"]}],
        "tool_calls": [],
        "policy_decisions": [{"decision": "deny"}],
        "events": ["message_received", "plan_created", "policy_decision"],
    },
    "applicable": True,
}
json.dump(output, sys.stdout)

