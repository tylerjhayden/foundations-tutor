"""Tutoring session: manages message history and cost tracking.

# Phase P2: streaming responses, cost cap enforcement.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TutorSession:
    paper_id: str
    model: str
    messages: list[dict] = field(default_factory=list)
    cost_usd: float = 0.0

    def send(self, user_message: str) -> str:
        raise NotImplementedError("Phase P2")

    def reset(self) -> None:
        self.messages.clear()
        self.cost_usd = 0.0
