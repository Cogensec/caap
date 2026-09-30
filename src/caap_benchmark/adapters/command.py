from __future__ import annotations

import json
import shlex
import subprocess
from typing import Any

from ..models import AdapterResponse
from .base import AgentAdapter
from .http import _normalize


class CommandAdapter(AgentAdapter):
    """Run an explicitly supplied local adapter command with the case on stdin."""

    name = "command"

    def __init__(self, command: str, timeout: float = 30.0):
        self.command = shlex.split(command)
        self.timeout = timeout

    def execute(self, test_case: dict[str, Any]) -> AdapterResponse:
        try:
            completed = subprocess.run(  # noqa: S603
                self.command,
                input=json.dumps({"caap_test": test_case}),
                text=True,
                capture_output=True,
                timeout=self.timeout,
                check=False,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            return AdapterResponse(events=[], error=str(exc))
        if completed.returncode != 0:
            detail = completed.stderr.strip()
            return AdapterResponse(
                events=[], error=f"adapter exited {completed.returncode}: {detail}"
            )
        try:
            payload = json.loads(completed.stdout)
        except json.JSONDecodeError as exc:
            return AdapterResponse(events=[], error=f"invalid adapter JSON: {exc}")
        return _normalize(payload)

