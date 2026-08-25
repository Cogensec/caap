from __future__ import annotations

import json
import urllib.error
import urllib.request
import urllib.parse
from typing import Any

from ..models import AdapterResponse, Event
from .base import AgentAdapter


class HttpAdapter(AgentAdapter):
    """POST a normalized CAAP case to an authorized local or test endpoint."""

    name = "http"

    def __init__(self, endpoint: str, timeout: float = 30.0, bearer_token: str | None = None, allow_remote: bool = False):
        self.endpoint = endpoint
        self.timeout = timeout
        self.bearer_token = bearer_token
        host = urllib.parse.urlparse(endpoint).hostname
        if not allow_remote and host not in {"127.0.0.1", "localhost", "::1"}:
            raise ValueError("remote endpoints are disabled by default; explicitly authorize remote testing")

    def execute(self, test_case: dict[str, Any]) -> AdapterResponse:
        body = json.dumps({"caap_test": test_case}).encode("utf-8")
        headers = {"Content-Type": "application/json", "User-Agent": "caap-benchmark/0.1"}
        if self.bearer_token:
            headers["Authorization"] = f"Bearer {self.bearer_token}"
        request = urllib.request.Request(self.endpoint, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:  # noqa: S310
                payload = json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            return AdapterResponse(events=[], error=str(exc))
        return _normalize(payload)


def _normalize(payload: dict[str, Any]) -> AdapterResponse:
    events = [Event.from_dict(value) for value in payload.get("events", [])]
    return AdapterResponse(
        events=events,
        response=str(payload.get("response", "")),
        telemetry=dict(payload.get("telemetry", {})),
        applicable=bool(payload.get("applicable", True)),
        error=payload.get("error"),
    )
