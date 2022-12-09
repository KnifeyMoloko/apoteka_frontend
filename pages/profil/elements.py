from pages.generic_element import ApotekElement


class ProfilUserName(ApotekElement):
    XPATH = "/html/body/div[2]/main/div[1]/div[1]/form/div[1]/input[1]"


class ProfilUserSurname(ApotekElement):
    XPATH = "/html/body/div[2]/main/div[1]/div[1]/form/div[1]/input[2]"


class ProfilEmailHeader(ApotekElement):
    XPATH = "/html/body/div[2]/main/div[1]/h1"
