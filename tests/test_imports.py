"""Smoke tests: verify all modules import cleanly."""

import foundations_tutor
from foundations_tutor import config
from foundations_tutor.catalog import models as catalog_models


def test_version():
    assert foundations_tutor.__version__ == "0.1.0"


def test_catalog_loads():
    parts = catalog_models.load_catalog()
    assert isinstance(parts, dict)


def test_relationships_load():
    rels = catalog_models.load_relationships()
    assert isinstance(rels, list)


def test_config_loads():
    cfg = config.load_config()
    assert cfg.tutor.model == "claude-sonnet-4-6"
