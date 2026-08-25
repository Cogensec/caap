from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from ..models import AdapterResponse


class AgentAdapter(ABC):
    """Boundary between the CAAP runner and an agent under authorized test."""

    name = "base"

    @abstractmethod
    def execute(self, test_case: dict[str, Any]) -> AdapterResponse:
        """Execute one case and return normalized, synthetic-only telemetry."""

