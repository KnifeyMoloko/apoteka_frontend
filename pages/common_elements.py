from pages.generic_element import ApotekElement


class CookieModalAcceptButton(ApotekElement):
    XPATH = "/html/body/div[1]/div/div/div[1]/div[3]/div[2]/button"


class LogIndMenulistLink(ApotekElement):
    XPATH = "/html/body/div[2]/header/div/div[3]/ul/li[1]/a"


class LogIndDropDownIcon(ApotekElement):
    XPATH = "/html/body/div[2]/header/div/div[3]/ul/li[1]/a/i"


class LogInLogoutButton(ApotekElement):
    XPATH = "/html/body/div[2]/header/div/div[3]/ul/li[1]/ul/li[7]/a"


class SearchBarInputField(ApotekElement):
    XPATH = "/html/body/div[2]/header/div/form/search/input"


class SearchBarSearchButton(ApotekElement):
    XPATH = "/html/body/div[2]/header/div/form/button"
