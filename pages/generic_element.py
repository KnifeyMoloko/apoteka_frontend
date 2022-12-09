from typing import NamedTuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ApotekElement:
    XPATH: str

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def wait_for_presence(self, timeout: int = 2):
        element = WebDriverWait(self._driver, timeout).until(ec.presence_of_element_located((By.XPATH, self.XPATH)))
        return element
