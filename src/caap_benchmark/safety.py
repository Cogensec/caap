from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Callable

SENTINEL_PATTERN = re.compile(r"^CAAP_[A-Z]{2}_[0-9]{2}_SENTINEL$")


class SafetyViolation(ValueError):
    pass


@dataclass
class SyntheticSink:
    """In-memory sink that accepts only CAAP sentinel tokens and performs no I/O."""

    name: str = "mock_forbidden_sink"
    records: list[str] = field(default_factory=list)

    def record(self, value: str) -> dict[str, Any]:
        if not SENTINEL_PATTERN.fullmatch(value):
            raise SafetyViolation("synthetic sink accepts CAAP sentinel tokens only")
        self.records.append(value)
        return {"sink": self.name, "sentinel": value, "synthetic": True}


@dataclass
class MockTool:
    name: str
    handler: Callable[[dict[str, Any]], dict[str, Any]]
    calls: list[dict[str, Any]] = field(default_factory=list)

    def invoke(self, arguments: dict[str, Any]) -> dict[str, Any]:
        copied = dict(arguments)
        self.calls.append(copied)
        return self.handler(copied)


class MockToolRegistry:
    """Explicit allowlist of in-memory tools exposed to a benchmark target."""

    def __init__(self) -> None:
        self._tools: dict[str, MockTool] = {}

    def register(self, tool: MockTool) -> None:
        if tool.name in self._tools:
            raise SafetyViolation(f"duplicate mock tool: {tool.name}")
        self._tools[tool.name] = tool

    def invoke(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        if name not in self._tools:
            raise SafetyViolation(f"tool is not in the mock allowlist: {name}")
        return self._tools[name].invoke(arguments)

    @property
    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._tools))

