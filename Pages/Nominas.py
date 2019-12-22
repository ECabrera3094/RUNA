import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        # --------------------
        self.XPath_Comenzar = MyLocators.XPath_Button_Comenzar
        self.CSS_Detail_Employee_1 = MyLocators.CSS_Detail_Employee_1
        self.XPath_Enter_New_Salary = MyLocators.XPath_Enter_New_Salary
        self.XPath_Button_Accept_Modify_Salary = MyLocators.XPath_Button_Accept_Modify_Salary
        self.CSS_Detail_Employee_3 = MyLocators.CSS_Detail_Employee_3
        self.XPath_Delete_Employee = MyLocators.XPath_Delete_Employee
        self.CSS_Confirm_Delete = MyLocators.CSS_Confirm_Delete
        # --------------------
        self.XPath_Button_Continuar = MyLocators.XPath_Button_Continuar
        self.ID_Checkbox_Seleccionar_Todos = MyLocators.ID_Checkbox_Seleccionar_Todos
        self.XPath_Link_Calcular = MyLocators.XPath_Link_Calcular
        self.XPath_Delete_Nomina = MyLocators.XPath_Delete_Nomina

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
        for i in range (0,6):
            textBox_Date_Incidence = self.driver.find_element_by_css_selector(self.CSS_Navigation_Horizontal).click()
            time.sleep(0.5)
        textBox_Date_Incidence = self.driver.find_element_by_css_selector(self.CSS_Day_From).click()
        time.sleep(0.5)
        textBox_Date_Incidence = self.driver.find_element_by_css_selector(self.CSS_Day_To).click()

    def click_Acept_New_Manual_Nomina(self):
        button_Acept = self.driver.find_element_by_xpath(self.XPath_Acept_New_Manual_Nomina).click()
        time.sleep(0.5)

    def click_Comenzar_Button(self):
        button_Comenzar = self.driver.find_element_by_xpath(self.XPath_Comenzar).click()
        time.sleep(0.5)

    def click_Detail_Employee_1(self):
        button_Details = self.driver.find_element_by_css_selector(self.CSS_Detail_Employee_1).click()
        time.sleep(3)

    def click_Modify_Salary(self):
        myAction = ActionChains(self.driver)
        # myAction.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(0.5)
        textBox_Enter_New_Salary = self.driver.find_element_by_xpath(self.XPath_Enter_New_Salary)
        length = len(textBox_Enter_New_Salary.text)
        myAction.click_and_hold(textBox_Enter_New_Salary)
        myAction.send_keys_to_element(textBox_Enter_New_Salary, (length * Keys.BACKSPACE) ).pause(1).send_keys("50000").send_keys(Keys.ENTER)
        myAction.perform()
        time.sleep(5)

    def click_Accept_Modify_Salary(self):
        button_Accept = self.driver.find_element_by_xpath(self.XPath_Button_Accept_Modify_Salary)
        if button_Accept.is_enabled():
            button_Accept.click()
            time.sleep(3)
        else:
            click_Modify_Salary()

    def click_Detail_Employee_3(self):
        button_Details = self.driver.find_element_by_css_selector(self.CSS_Detail_Employee_3).click()
        time.sleep(3)

    def click_Delete_Employee(self):
        link_Delete_Employee = self.driver.find_element_by_xpath(self.XPath_Delete_Employee).click()
        time.sleep(0.5)
        button_Accept_Delete = self.driver.find_element_by_css_selector(self.CSS_Confirm_Delete).click()
        time.sleep(0.5)
        try:
            search_Textbox = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "search"))
            )
        except:
            self.driver.refresh()

    def click_Continuar(self):
        button_Continuar = self.driver.find_element_by_xpath(self.XPath_Button_Continuar).click()
        time.sleep(3)

    def click_Uncheckbox(self):
        checkbox_Seleccionar_Todos = self.driver.find_element_by_id(self.ID_Checkbox_Seleccionar_Todos).click()
        time.sleep(0.5)

    def click_Calcular(self):
        link_Calcular = self.driver.find_element_by_xpath(self.XPath_Link_Calcular).click()
        time.sleep(5)
        try:
            search_Textbox = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "search"))
            )
        except:
            self.driver.refresh()

    def click_Delete_Nomina(self):
        link_Delete_Nomina = self.driver.find_element_by_xpath(self.XPath_Delete_Nomina).click()
        time.sleep(0.5)
        button_Accept_Delete = self.driver.find_element_by_css_selector(self.CSS_Confirm_Delete).click()
        time.sleep(0.5)
