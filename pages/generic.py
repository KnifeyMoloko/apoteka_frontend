from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver


class Page(ABC):
    def __init__(self, driver: WebDriver, url: str = ""):
        self._url = url
        self._driver = driver

    @property
    def driver(self) -> WebDriver:
        return self._driver

    @property
    def url(self) -> str:
        return self._url

    def get(self):
        return self.driver.get(self.url)
