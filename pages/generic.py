import logging
from abc import ABC

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.common_elements import (
    CookieModalAcceptButton,
    LogIndDropDownIcon,
    LogInLogoutButton,
    SearchBarInputField,
    SearchBarSearchButton,
)


class Page(ABC):
    def __init__(self, driver: WebDriver, url: str = "", *args, **kwargs):
        self._url = url
        self._driver = driver
        self._logger = logging.getLogger(self.__class__.__name__)

    @property
    def driver(self) -> WebDriver:
        return self._driver

    @property
    def url(self) -> str:
        return self._url

    def get(self):
        self._logger.info("Getting page from URL: %s", self.url)
        return self.driver.get(self.url)

    def get_cookie_modal_accept_button(self) -> WebElement:
        return CookieModalAcceptButton(self.driver).wait_for_clickable()

    def click_cookie_modal_accept_button(self) -> None:
        self._logger.info("Clicking on the Cookie Modal Accept Button...")
        cookie_modal_accept_button = self.get_cookie_modal_accept_button()
        cookie_modal_accept_button.click()
        self._logger.info("Clicked on the Cookie Modal Accept Button.")

    def get_log_ind_dropdown(self) -> WebElement:
        return LogIndDropDownIcon(self.driver).wait_for_clickable()

    def click_log_ind_dropdown(self) -> None:
        log_ind_dropdown = self.get_log_ind_dropdown()
        log_ind_dropdown.click()

    def get_log_ind_logout_button(self) -> WebElement:
        return LogInLogoutButton(self.driver).wait_for_clickable()

    def get_search_bar_input_field(self) -> WebElement:
        return SearchBarInputField(self.driver).wait_for_clickable()

    def get_search_bar_search_button(self) -> WebElement:
        return SearchBarSearchButton(self.driver).wait_for_clickable()

    def search_for_items(self, query_string: str):
        self._logger.info("Starting 'Search for items procedure'...")
        search_bar_input_field = self.get_search_bar_input_field()
        search_bar_search_button = self.get_search_bar_search_button()

        self._logger.info(
            "Sending query string: %s to search bar input field...", query_string
        )
        search_bar_input_field.send_keys(query_string)
        self._logger.info(
            "Submitting search bar request by clicking the magnifying glass button..."
        )
        search_bar_search_button.click()

    def logout(self) -> None:
        log_ind_dropdown = self.get_log_ind_dropdown()
        log_ind_dropdown.click()
        logout_button = self.get_log_ind_logout_button()
        logout_button.click()
