import os
import logging
from pathlib import Path
from datetime import datetime

import pytest
from selenium.webdriver import Chrome

from users.user import TestUser

logging.basicConfig(
    filename=Path(f"logs/{datetime.timestamp(datetime.now())}.log"),
    encoding="utf-8",
    level=logging.DEBUG,
)


@pytest.fixture
def chrome_driver():
    chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
    logging.info("Loading Chrome driver from path: %s", chrome_driver_path)
    return Chrome(executable_path=Path(chrome_driver_path))


@pytest.fixture
def regular_user():
    return TestUser.from_yaml("regular_user")
