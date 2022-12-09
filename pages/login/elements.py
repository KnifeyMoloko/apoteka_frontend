from pages.generic_element import ApotekElement


class LoginForm(ApotekElement):
    XPATH = "/html/body/div[2]/main/div[1]/div/div[1]/form"


class LoginFormEmailField(ApotekElement):
    XPATH = "/html/body/div[2]/main/div[1]/div/div[1]/form/div[1]/input[1]"


class LoginFormPasswordField(ApotekElement):
    XPATH = "/html/body/div[2]/main/div[1]/div/div[1]/form/div[1]/input[2]"


class LoginFormSubmitButton(ApotekElement):
    XPATH = "/html/body/div[2]/main/div[1]/div/div[1]/form/div[2]/input"
