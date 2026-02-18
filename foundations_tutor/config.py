"""App configuration: loads default_config.yaml + first-run ~/.foundations-tutor/ setup.

Phase P1: first-run directory creation and config loading.
"""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, Field

CONFIG_DIR = Path.home() / ".foundations-tutor"
USER_CONFIG = CONFIG_DIR / "config.yaml"
DEFAULT_CONFIG = Path(__file__).parent / "data" / "default_config.yaml"


class MasteryThresholds(BaseModel):
    introduced: int = 1
    practicing: float = 0.60
    proficient: float = 0.70
    mastered: float = 0.80
    teaching: int = 14


class TutorConfig(BaseModel):
    model: str = "claude-sonnet-4-6"
    session_cost_cap: float = 1.00
    cost_warning_threshold: float = 0.80
    mastery_thresholds: MasteryThresholds = Field(default_factory=MasteryThresholds)


class MathConfig(BaseModel):
    starting_level: str = "high_school"
    physics_analogies: bool = True


class DisplayConfig(BaseModel):
    read_only_without_key: bool = True


class AppConfig(BaseModel):
    tutor: TutorConfig = Field(default_factory=TutorConfig)
    math: MathConfig = Field(default_factory=MathConfig)
    display: DisplayConfig = Field(default_factory=DisplayConfig)
    identity_file: str | None = None


def _first_run_setup() -> None:
    """Create ~/.foundations-tutor/ with defaults if it doesn't exist."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if not USER_CONFIG.exists():
        import shutil

        shutil.copy(DEFAULT_CONFIG, USER_CONFIG)


def load_config() -> AppConfig:
    """Load config from ~/.foundations-tutor/config.yaml, creating it on first run."""
    _first_run_setup()
    raw = yaml.safe_load(USER_CONFIG.read_text())
    return AppConfig.model_validate(raw)
