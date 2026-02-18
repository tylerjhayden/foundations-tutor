"""Catalog data models: Paper, Part, Relationship.

Phase P1: loads catalog.yaml + relationships.yaml for the catalog page.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

DATA_DIR = Path(__file__).parent.parent / "data"


@dataclass
class Paper:
    id: str
    title: str
    year: int
    authors: list[str] = field(default_factory=list)
    arxiv: str | None = None
    tags: list[str] = field(default_factory=list)


@dataclass
class Part:
    id: str
    title: str
    description: str = ""
    papers: list[Paper] = field(default_factory=list)


@dataclass
class Relationship:
    source: str  # paper id
    target: str  # paper id
    kind: str  # "builds_on", "contrasts_with", etc.


def load_catalog() -> dict[str, Part]:
    """Load parts and papers from data/catalog.yaml."""
    raw = yaml.safe_load((DATA_DIR / "catalog.yaml").read_text()) or {}
    parts: dict[str, Part] = {}
    for part_id, part_data in (raw.get("parts") or {}).items():
        papers = [
            Paper(
                id=p["id"],
                title=p["title"],
                year=p.get("year", 0),
                authors=p.get("authors", []),
                arxiv=p.get("arxiv"),
                tags=p.get("tags", []),
            )
            for p in (part_data.get("papers") or [])
        ]
        parts[part_id] = Part(
            id=part_id,
            title=part_data.get("title", part_id),
            description=part_data.get("description", ""),
            papers=papers,
        )
    return parts


def load_relationships() -> list[Relationship]:
    """Load concept relationships from data/relationships.yaml."""
    raw = yaml.safe_load((DATA_DIR / "relationships.yaml").read_text()) or {}
    return [
        Relationship(source=e["source"], target=e["target"], kind=e.get("kind", "builds_on"))
        for e in (raw.get("edges") or [])
    ]
