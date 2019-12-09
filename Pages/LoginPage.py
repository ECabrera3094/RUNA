from Locators.Locators import MyLocators

class MyLoginPage():

    # Constructor
    def __init__(self,driver):
        self.driver = driver
        self.ID_Username = MyLocators.ID_Username
        self.ID_Password = MyLocators.ID_Password
        self.XPath_Button = MyLocators.XPath_Button

    # Método de Instancia == Accion.
    def enter_Username(self, strUsername):
        textBox_Username = self.driver.find_element_by_id(self.ID_Username).send_keys(strUsername)

    def enter_Password(self, strPasswordd):
        textBox_Password = self.driver.find_element_by_id(self.ID_Password).send_keys(strPasswordd)

    def click_Button(self):
        button_Login = self.driver.find_element_by_xpath(self.XPath_Button).click()
