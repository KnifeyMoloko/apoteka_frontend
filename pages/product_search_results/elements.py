from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.generic_element import ApotekElement


class ProductBuyButton(ApotekElement):
    XPATH = None
    CLASS = "enable-add"

    def get_all_buy_buttons(self) -> list[WebElement] | None:
        self._logger.info("Searching for product buy buttons...")
        return self._driver.find_elements(by=By.CLASS_NAME, value=self.CLASS)


class BuyConfirmationModalAddToCartButton(ApotekElement):
    XPATH = "/html/body/div[4]/div/div/div/div[2]/div/div[3]/div/div[2]/p[1]/a"
