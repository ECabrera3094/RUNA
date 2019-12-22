from Locators.Locators import MyLocators

class MyMainWindow():

    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.XPath_Cancel_ChangePassword = MyLocators.XPath_Cancel_ChangePassword
        self.XPath_Nominas = MyLocators.XPath_Nominas
        self.Class_Close_Video = MyLocators.Class_Close_Video
        self.Text_Nominas_Activaas = MyLocators.Text_Nominas_Activas

    # Método de Instancia == Acción.
    def click_ChangePassword(self):
        button_Cancel = self.driver.find_element_by_xpath(self.XPath_Cancel_ChangePassword).click()

    def click_Nominas(self):
        link_Nominas = self.driver.find_element_by_xpath(self.XPath_Nominas).click()

    def click_Close_Video(self):
        close_Video_Nominas = self.driver.find_element_by_class_name(self.Class_Close_Video).click()

    def click_Nominas_Activas(self):
        click_Nominas_Activas = self.driver.find_element_by_link_text(self.Text_Nominas_Activaas).click()
