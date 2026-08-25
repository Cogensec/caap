#!/usr/bin/env python3
"""Localhost-only adapter-contract example for development and CI."""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", "0"))
        case = json.loads(self.rfile.read(length))["caap_test"]
        payload = {
            "response": "Untrusted synthetic fixture denied.",
            "events": [
                {"type": "message_received", "data": {"trust": "untrusted"}},
                {"type": "plan_created", "data": {"objective": case["benign_objective"]}},
                {"type": "policy_decision", "data": {"decision": "deny"}},
            ],
            "telemetry": {
                "messages": [{"trust": "untrusted"}],
                "plans": [{"objective": case["benign_objective"]}],
                "tool_calls": [],
                "policy_decisions": [{"decision": "deny"}],
                "events": ["message_received", "plan_created", "policy_decision"],
            },
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

