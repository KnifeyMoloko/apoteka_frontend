from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.generic import Page
from pages.profil.elements import ProfilUserName, ProfilUserSurname, ProfilEmailHeader


class ProfilPage(Page):
    def __init__(self, driver: WebDriver, *args, **kwargs):
        super().__init__(url="https://apopro.dk/Profile", driver=driver, kwargs=kwargs)
        self.title = "Profil | Apopro.dk"

    def get_profil_user_name_field(self) -> WebElement:
        return ProfilUserName(self.driver).wait_for_presence()

    def get_profil_user_surname_field(self) -> WebElement:
        return ProfilUserSurname(self.driver).wait_for_presence()

    def get_profil_user_email_header(self) -> WebElement:
        return ProfilEmailHeader(self.driver).wait_for_presence()
