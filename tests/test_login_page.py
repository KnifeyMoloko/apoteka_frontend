import pytest
from assertpy import assert_that

from pages.login.page import LoginPage
from pages.profil.page import ProfilPage
from utils.common import get_page


@pytest.fixture(scope="function")
def login_page_model(chrome_driver) -> LoginPage:
    return get_page(page_model=LoginPage, driver=chrome_driver)


@pytest.fixture(scope="function")
def profil_page_model(chrome_driver) -> ProfilPage:
    return get_page(page_model=ProfilPage, driver=chrome_driver)


def test_login_regular_user(login_page_model, profil_page_model, regular_user):
    login_page_model.click_cookie_modal_accept_button()
    assert_that(login_page_model.get_login_form_email_input_field()).is_not_none()
    assert_that(login_page_model.get_login_form_password_input_field()).is_not_none()
    assert_that(login_page_model.get_login_form_submit_button()).is_not_none()

    assert_that(login_page_model.driver.title).is_equal_to(login_page_model.title)
    login_page_model.login(user=regular_user)

    assert_that(login_page_model.driver.title).is_equal_to(profil_page_model.title)

    assert_that(profil_page_model.get_profil_user_email_header().text).contains(
        regular_user.email
    )
    assert_that(
        profil_page_model.get_profil_user_name_field().get_property("value")
    ).is_equal_to(regular_user.name)
    assert_that(
        profil_page_model.get_profil_user_surname_field().get_property("value")
    ).is_equal_to(regular_user.surname)
