from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.generic import Page
from pages.login.elements import (
    LoginFormEmailField,
    LoginFormPasswordField,
    LoginFormSubmitButton,
    LoginForm,
)
from users.user import TestUser


class LoginPage(Page):
    def __init__(self, driver: WebDriver, *args, **kwargs):
        super().__init__(
            url="https://apopro.dk/Account/Login", driver=driver, kwargs=kwargs
        )
        self.title = "Login | Apopro.dk"

    def get_login_form(self) -> WebElement:
        return LoginForm(driver=self.driver).wait_for_presence()

    def get_login_form_email_input_field(self) -> WebElement:
        return LoginFormEmailField(driver=self.driver).wait_for_presence()

    def get_login_form_password_input_field(self) -> WebElement:
        return LoginFormPasswordField(driver=self.driver).wait_for_presence()

    def get_login_form_submit_button(self) -> WebElement:
        return LoginFormSubmitButton(driver=self.driver).wait_for_clickable()

    def login(self, user: TestUser):
        self._logger.info("Running the log-in procedrure...")
        email_field = self.get_login_form_email_input_field()
        password_field = self.get_login_form_password_input_field()
        submit_button = self.get_login_form_submit_button()

        self._logger.info("Sending log-in form keys...")
        email_field.send_keys(user.email)
        password_field.send_keys(user.passwd)
        self._logger.info("Clicking the login button...")
        submit_button.click()
        self._logger.info("Log-in procedure completed")
