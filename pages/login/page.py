from selenium.webdriver.remote.webdriver import WebDriver

from pages.generic import Page


class LoginPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(url="https://apopro.dk/Account/Login", driver=driver)
        self.title = "Login | Apopro.dk"

