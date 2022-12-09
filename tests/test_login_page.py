from assertpy import assert_that

import pytest

from pages.login.page import LoginPage
from utils.common import get_page


@pytest.fixture(scope="function")
def login_page_model(chrome_driver):
    return get_page(page_model=LoginPage, driver=chrome_driver)

