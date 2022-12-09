from assertpy import assert_that

import pytest

from pages.landing.elements import CookieModalAcceptButton, LogIndMenulistLink
from pages.landing.page import LandingPage
from utils.common import get_page


@pytest.fixture(scope="function")
def landing_page_model(chrome_driver) -> LandingPage:
    return get_page(LandingPage, driver=chrome_driver)


def test_page_title(landing_page_model):
    assert_that(landing_page_model.driver.title).is_equal_to(landing_page_model.title)


def test_click_login_page_link(landing_page_model):
    cookie_modal_accept_button = CookieModalAcceptButton(landing_page_model.driver).wait_for_presence()
    log_ing_menulist_link = LogIndMenulistLink(landing_page_model.driver).wait_for_presence()
    cookie_modal_accept_button.click()
    log_ing_menulist_link.click()
    assert_that(landing_page_model.driver.current_url).is_equal_to("https://apopro.dk/Account/Login")
