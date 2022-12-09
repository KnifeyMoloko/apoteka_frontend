import logging
from abc import ABC

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.common_elements import CookieModalAcceptButton


class Page(ABC):
    def __init__(self, driver: WebDriver, url: str = ""):
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
