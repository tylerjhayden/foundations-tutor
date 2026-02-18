"""Tutoring agent powered by Claude.

# Phase P2: implement multi-turn Socratic tutoring with tool use.
"""
from __future__ import annotations


class TutorAgent:
    """Drives a tutoring session using Claude."""

    def __init__(self, model: str, api_key: str) -> None:
        self.model = model
        self.api_key = api_key

    def start_session(self, paper_id: str, identity: str | None = None) -> "TutorSession":  # noqa: F821
        raise NotImplementedError("Phase P2")
