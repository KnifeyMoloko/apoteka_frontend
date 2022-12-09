from pages.generic_element import ApotekElement


class CookieModalAcceptButton(ApotekElement):
    XPATH = "/html/body/div[1]/div/div/div[1]/div[3]/div[2]/button"


class LogIndMenulistLink(ApotekElement):
    XPATH = "/html/body/div[2]/header/div/div[3]/ul/li[1]/a"
