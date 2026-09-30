#!/usr/bin/env python3
"""Localhost-only adapter-contract example for development and CI.

The server replays the case's declared secure trace so the HTTP contract can be
exercised end to end. A real adapter MUST derive events from the target's own
trace; replaying the declared trace proves nothing about an agent.
"""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from caap_benchmark.events import telemetry_from_events


class Handler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", "0"))
        case = json.loads(self.rfile.read(length))["caap_test"]
        trace = case.get("mock_scenario", {}).get("safe")
        if trace:
            events = trace["events"]
            response = trace["response"]
        else:
            events = [
                {"type": "message_received", "data": {"trust": "untrusted"}},
                {"type": "plan_created", "data": {"objective": case["benign_objective"]}},
                {"type": "policy_decision", "data": {"decision": "deny"}},
            ]
            response = "Untrusted synthetic fixture denied."
        payload = {
            "response": response,
            "events": events,
            "telemetry": telemetry_from_events(events),
        }
        encoded = json.dumps(payload).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, format: str, *args: object) -> None:
        return


if __name__ == "__main__":
    print("Safe CAAP example adapter listening on http://127.0.0.1:8765")
    ThreadingHTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
