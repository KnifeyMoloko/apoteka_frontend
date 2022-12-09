from typing import Generator

import pytest
from assertpy import assert_that

from pages.basket.page import ProductBasketPage
from pages.login.page import LoginPage
from pages.product_search_results.page import ProductSearchPage
from pages.profil.page import ProfilPage
from utils.common import get_page


@pytest.fixture(scope="function")
def login_page_model(chrome_driver) -> LoginPage:
    return get_page(page_model=LoginPage, driver=chrome_driver)


@pytest.fixture(scope="function")
def profil_page_model(chrome_driver) -> Generator[ProfilPage, None, None]:
    return ProfilPage(driver=chrome_driver)


@pytest.fixture(scope="function")
def product_search_results_page(
    chrome_driver,
) -> Generator[ProductSearchPage, None, None]:
    page_model = ProductSearchPage(driver=chrome_driver, query_string="Strepsils")
    yield page_model


@pytest.fixture(scope="function")
def product_basket_page(chrome_driver) -> Generator[ProductBasketPage, None, None]:
    page_model = ProductBasketPage(driver=chrome_driver)
    yield page_model
    page_model.logout()


@pytest.fixture(scope="function")
def login(login_page_model, regular_user) -> Generator[LoginPage, None, None]:
    login_page_model.click_cookie_modal_accept_button()
    login_page_model.login(regular_user)
    yield


def test_login_search_add_and_remove_items_from_basket(
    login, profil_page_model, product_search_results_page, product_basket_page
):
    """
    A simple flow test.
    1. Start with a session of a logged in user (from the Profil page).
    2. Enter a search for 'Strepsils' into the search bar and confirm by
    clicking the search button.
    3. Add the first item for the search results (we don't care what the
    specific item is here, as long as there is one).
    4. Confirm the selection.
    5.  Check that the basket details page we landed on shows the
    correct counter for our selected item.
    6. Remove the item by clicking on the "Empty Bakset" button.
    7. Check that the page loads in a message about the basket
    being empty.
    8. Check that the item counter at the basket icon now has a value of
    zero.
    """
    profil_page_model.search_for_items("Strepsils")
    product_search_results_page.click_random_buy_button()
    product_search_results_page.click_buy_confirmation_modal_add_to_cart_button()
    product_counter_before = int(product_basket_page.get_cart_product_counter().text)
    product_basket_page.empty_product_basket()
    cart_is_empty_message = product_basket_page.get_cart_empty_message()

    assert_that(product_counter_before).is_equal_to(1)
    assert_that(cart_is_empty_message).is_not_none()
    assert_that(product_basket_page.get_cart_product_counter().text).is_equal_to(
        product_counter_before - 1
    )
