"""Spaced repetition progress tracking using FSRS.

# Phase P3: per-user FSRS card state, persistence to ~/.foundations-tutor/progress/.
"""
from __future__ import annotations


class ProgressTracker:
    """Tracks mastery state for each paper/concept using FSRS v6 Scheduler."""

    def __init__(self, data_dir: str) -> None:
        self.data_dir = data_dir

    def get_due_cards(self) -> list[dict]:
        raise NotImplementedError("Phase P3")

    def record_review(self, card_id: str, rating: int) -> None:
        raise NotImplementedError("Phase P3")

    def mastery_level(self, card_id: str) -> str:
        """Returns: introduced | practicing | proficient | mastered | teaching"""
        raise NotImplementedError("Phase P3")
