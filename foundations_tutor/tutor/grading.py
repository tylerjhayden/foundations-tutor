"""Grades user responses and maps to FSRS rating.

# Phase P2: LLM-based grading rubric with 0–4 rating output.
"""
from __future__ import annotations


def grade_response(question: str, user_answer: str, model_answer: str) -> int:
    """Return FSRS rating 1–4. Raises NotImplementedError until Phase P2."""
    raise NotImplementedError("Phase P2")
