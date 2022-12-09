import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class ApotekElement:
    XPATH: str

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._logger = logging.getLogger(self.__class__.__name__)

    def wait_for_presence(self, timeout: int = 2):
        self._logger.debug("Waiting for presence of element...")
        element = WebDriverWait(self._driver, timeout).until(
            ec.presence_of_element_located((By.XPATH, self.XPATH))
        )
        return element

    def wait_for_clickable(self, timeout: int = 2):
        self._logger.debug("Watiing for element to become clickable...")
        element = WebDriverWait(self._driver, timeout).until(
            ec.element_to_be_clickable((By.XPATH, self.XPATH))
        )
        return element
