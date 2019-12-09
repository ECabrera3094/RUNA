import time
from selenium.webdriver.common.keys import Keys

from Locators.Locators import MyLocators

class MyNominas_Activas():

    def __init__(self, driver):
        self.driver = driver
        self.XPath_Button_Nueva_Nomina = MyLocators.XPath_Button_Nueva_Nomina
        self.CSS_Nomina_Group = MyLocators.CSS_Nomina_Group
        self.ID_Nomina_Group = MyLocators.ID_Nomina_Group
        # --------------------
        self.ID_Start_Date = MyLocators.ID_Start_Date
        self.CSS_Navigation_Previous = MyLocators.CSS_Navigation_Previous
        self.CSS_Day = MyLocators.CSS_Day
        # --------------------
        self.ID_Date_Incidence = MyLocators.ID_Date_Incidence
        self.CSS_Navigation_Horizontal = MyLocators.CSS_Navigation_Horizontal
        self.CSS_Day_From = MyLocators.CSS_Day_From
        self.CSS_Day_To = MyLocators.CSS_Day_To
        self.XPath_Acept_New_Manual_Nomina = MyLocators.XPath_Acept_New_Manual_Nomina

    def click_Nueva_Nomina(self):
        click_Nueva_Nomina = self.driver.find_element_by_xpath(self.XPath_Button_Nueva_Nomina).click()

    def enter_Nomina_Group(self):
        textBox_Nomina_Group = self.driver.find_element_by_css_selector(self.CSS_Nomina_Group).click()
        textBox_Nomina_Group = self.driver.find_element_by_id(self.ID_Nomina_Group).send_keys("Guacamole")
        textBox_Nomina_Group = self.driver.find_element_by_id(self.ID_Nomina_Group).send_keys(Keys.ENTER)

    def enter_Start_Date(self):
        textBox_Star_Date = self.driver.find_element_by_id(self.ID_Start_Date).click()
        for i in range(0,6):
            textBox_Star_Date = self.driver.find_element_by_css_selector(self.CSS_Navigation_Previous).click()
            time.sleep(0.5)
        textBox_Star_Date = self.driver.find_element_by_css_selector(self.CSS_Day).click()

    def enter_Date_Incidence(self):
        textBox_Date_Incidence = self.driver.find_element_by_id(self.ID_Date_Incidence).click()
        for i in range (0,7):
            textBox_Date_Incidence = self.driver.find_element_by_css_selector(self.CSS_Navigation_Horizontal).click()
            time.sleep(0.5)
        textBox_Date_Incidence = self.driver.find_element_by_css_selector(self.CSS_Day_From).click()
        textBox_Date_Incidence = self.driver.find_element_by_css_selector(self.CSS_Day_To).click()

    def click_Acept_New_Manual_Nomina(self):
        button_Acept = self.driver.find_element_by_xpath(self.XPath_Acept_New_Manual_Nomina).click()




