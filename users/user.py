from __future__ import annotations

import logging
from pathlib import Path
from typing import NamedTuple

import yaml

LOGGER = logging.getLogger("TestUser")


class TestUser(NamedTuple):
    name: str
    surname: str
    email: str
    passwd: str

    @staticmethod
    def from_yaml(test_user_name: str) -> TestUser:
        user_yaml_path = Path(f"users/{test_user_name}.yaml")

        with user_yaml_path.open(mode="r") as infile:
            LOGGER.debug(
                "Getting test user instance from YAML with path: %s",
                user_yaml_path.absolute(),
            )
            return TestUser(**yaml.safe_load(infile))
