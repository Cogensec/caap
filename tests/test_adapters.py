from __future__ import annotations

import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from caap_benchmark.adapters import HttpAdapter
from caap_benchmark.events import telemetry_from_events
from caap_benchmark.models import ResultState
from caap_benchmark.runner import BenchmarkRunner

ROOT = Path(__file__).resolve().parents[1]
CASE = json.loads((ROOT / "benchmarks/executable/gh/CAAP-GH-01.json").read_text(encoding="utf-8"))

SAFE_PAYLOAD = {
    "response": CASE["mock_scenario"]["safe"]["response"],
    "events": CASE["mock_scenario"]["safe"]["events"],
    "telemetry": telemetry_from_events(CASE["mock_scenario"]["safe"]["events"]),
}


class _LoopbackServer:
    """Localhost-only test server that records every request it receives."""

    def __init__(self, mode: str) -> None:
        self.requests: list[dict[str, str]] = []
        server = self

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self) -> None:  # noqa: N802
                length = int(self.headers.get("Content-Length", "0"))
                self.rfile.read(length)
                server.requests.append(
                    {"path": self.path, "authorization": self.headers.get("Authorization", "")}
                )
                if mode == "redirect":
                    self.send_response(302)
                    self.send_header("Location", "http://example.invalid/collect")
                    self.send_header("Content-Length", "0")
                    self.end_headers()
                    return
                body = json.dumps(SAFE_PAYLOAD).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, format: str, *args: object) -> None:
                return

        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)

    def __enter__(self) -> _LoopbackServer:
        self.thread.start()
        return self

    def __exit__(self, *exc: object) -> None:
        self.httpd.shutdown()
        self.httpd.server_close()

    @property
    def url(self) -> str:
        return f"http://127.0.0.1:{self.httpd.server_address[1]}/"


class HttpAdapterTests(unittest.TestCase):
    def test_remote_endpoint_is_refused_by_default(self) -> None:
        with self.assertRaises(ValueError):
            HttpAdapter("http://example.invalid/agent")

    def test_direct_json_reply_passes(self) -> None:
        with _LoopbackServer("ok") as server:
            result = BenchmarkRunner(HttpAdapter(server.url)).run(CASE)
        self.assertEqual(result.state, ResultState.PASS)
        self.assertEqual(len(server.requests), 1)

    def test_redirect_is_refused_and_not_followed(self) -> None:
        with _LoopbackServer("redirect") as server:
            adapter = HttpAdapter(server.url, bearer_token="synthetic-test-token")
            result = BenchmarkRunner(adapter).run(CASE)
        self.assertEqual(result.state, ResultState.TEST_ERROR)
        self.assertIsNotNone(result.error)
        self.assertIn("redirect refused", result.error or "")
        self.assertIn("example.invalid", result.error or "")
        self.assertEqual(len(server.requests), 1)
        self.assertEqual(server.requests[0]["authorization"], "Bearer synthetic-test-token")

    def test_redirect_is_refused_even_when_remote_is_allowed(self) -> None:
        with _LoopbackServer("redirect") as server:
            adapter = HttpAdapter(server.url, allow_remote=True)
            result = BenchmarkRunner(adapter).run(CASE)
        self.assertEqual(result.state, ResultState.TEST_ERROR)
        self.assertIn("redirect refused", result.error or "")


if __name__ == "__main__":
    unittest.main()
