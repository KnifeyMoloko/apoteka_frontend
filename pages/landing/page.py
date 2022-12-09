from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.generic import Page


class LandingPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(url="https://apopro.dk/", driver=driver)
        self.title = "Apopro online apotek | Receptpligtig medicin leveret til døren! ✓"

    def get_login_button(self) -> WebElement:
        pass

    def get_cookie_modal_button(self):
        return

