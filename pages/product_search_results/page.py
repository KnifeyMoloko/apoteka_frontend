import random

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.generic import Page
from pages.product_search_results.elements import (
    ProductBuyButton,
    BuyConfirmationModalAddToCartButton,
)


class ProductSearchPage(Page):
    def __init__(self, driver: WebDriver, **kwargs):
        super().__init__(
            url=f"https://apopro.dk/search?query={kwargs.get('query_string')}",
            driver=driver,
        )
        self.title = "Søg | Apopro.dk"

    def get_search_results_buy_buttons(self) -> list[WebElement]:
        self._logger.info("Getting all of the buy buttons...")
        buy_buttons = ProductBuyButton(self.driver).get_all_buy_buttons()
        self._logger.info("Found these buy buttons: %s", buy_buttons)
        return buy_buttons

    def get_random_buy_button(self) -> WebElement:
        self._logger.info(
            "Getting a random buy button from all of the ones on the page..."
        )
        return random.choice(self.get_search_results_buy_buttons())

    def get_buy_confirmation_modal_add_to_cart_button(self) -> WebElement:
        return BuyConfirmationModalAddToCartButton(self.driver).wait_for_clickable()

    def click_random_buy_button(self) -> None:
        self._logger.info("Clicking random buy button...")
        self.get_random_buy_button().click()

    def click_buy_confirmation_modal_add_to_cart_button(self):
        confirmation_button = self.get_buy_confirmation_modal_add_to_cart_button()
        confirmation_button.click()
