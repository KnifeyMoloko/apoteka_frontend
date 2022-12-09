from pages.generic_element import ApotekElement


class EmptyBasketButton(ApotekElement):
    XPATH = "/html/body/div[2]/main/div[2]/main/div[3]/div[1]/div/div[2]/div/div[2]/div[1]/a"


class CartEmptyMessage(ApotekElement):
    XPATH = "/html/body/div[2]/main/div[2]/main/div[2]"


class CartIconProductCounter(ApotekElement):
    XPATH = "/html/body/div[2]/header/div/div[3]/ul/li[3]/a/em"
