import os
import time
from pathlib import Path

from assertpy import assert_that
from selenium.webdriver import Chrome

import pytest

from pages.landing.elements import CookieModalAcceptButton, LogIndMenulistLink
from pages.landing.page import LandingPage


@pytest.fixture(scope="module")
def chrome_driver():
    return Chrome(executable_path=Path(os.getenv("CHROME_DRIVER_PATH")))


@pytest.fixture(scope="function")
def landing_page_model(chrome_driver):
    landing_page = LandingPage(chrome_driver)
    landing_page.get()
    return landing_page


def test_page_title(landing_page_model):
    landing_page_model.get()
    assert_that(landing_page_model.driver.title).is_equal_to(landing_page_model.title)


def test_click_login_page(landing_page_model):
    landing_page_model.get()
    cookie_modal_accept_button = CookieModalAcceptButton(landing_page_model.driver).wait_for_presence()
    log_ing_menulist_link = LogIndMenulistLink(landing_page_model.driver).wait_for_presence()
    cookie_modal_accept_button.click()
    log_ing_menulist_link.click()
    assert_that(landing_page_model.driver.current_url).is_equal_to("https://apopro.dk/Account/Login")
