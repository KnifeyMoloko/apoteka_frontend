from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.basket.elements import (
    EmptyBasketButton,
    CartIconProductCounter,
    CartEmptyMessage,
)
from pages.generic import Page


class ProductBasketPage(Page):
    def __init__(self, driver: WebDriver, **kwargs):
        super().__init__(url=f"https://apopro.dk/Cart", driver=driver)
        self.title = "Kurv | Apopro.dk"

    def get_empty_basket_button(self) -> WebElement:
        return EmptyBasketButton(self.driver).wait_for_clickable()

    def get_cart_product_counter(self) -> WebElement | None:
        try:
            cart_product_counter = CartIconProductCounter(
                self.driver
            ).wait_for_presence()
        except TimeoutException as texc:
            self._logger.warning(
                "Timed out while waiting for presence of CartProductCounter. "
                "Full exception:\n%s",
                texc,
            )
            return None
        return cart_product_counter

    def get_cart_empty_message(self) -> WebElement:
        return CartEmptyMessage(self.driver).wait_for_presence()

    def empty_product_basket(self) -> None:
        self._logger.info("Emptying the product basket...")
        empty_basket_button = self.get_empty_basket_button()
        empty_basket_button.click()
        self._logger.info("Product basket emptied.")
