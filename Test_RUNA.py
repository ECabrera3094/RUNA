import time
import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.LoginPage import MyLoginPage
from Pages.LogoutPage import MyLogoutPage
from Pages.MainWindow import MyMainWindow
from Pages.Nominas import MyNominas_Activas
from Locators.Locators import MyLocators

class RUNA(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"C:/Users/768136/Downloads/chromedriver.exe")
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

    def test_RUNA(self):
        driver = self.driver
        driver.get("http://automation.runademos.info/login")

        # Explicit Wait
        try:
            textbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
        except:
            driver.refresh()

        # Creamos el Objeto 'login' INSTANCIANDO a la Clase MyLoginPage().
        login = MyLoginPage(driver)
        login.enter_Username("producto+automation@runahr.com")
        login.enter_Password("runahr")
        login.click_Button()

        time.sleep(10)

        # Creamos el Objeto 'mainWindow' INSTANCIANDO a la Clase MyMainWindow().
        mainWindow = MyMainWindow(driver)
        #mainWindow.click_ChangePassword()
        mainWindow.click_Nominas()
        mainWindow.click_Close_Video()
        mainWindow.click_Nominas_Activas()

        # Creamos el Objeto 'nomina' INSTANCIANDO a la Clase MyNominas_Activas().
        nominas = MyNominas_Activas(driver)
        nominas.click_Nueva_Nomina()
        nominas.enter_Nomina_Group()
        nominas.enter_Start_Date()
        nominas.enter_Date_Incidence()
        nominas.click_Acept_New_Manual_Nomina()
        nominas.click_Comenzar_Button()

        # Explicit Wait - Search TextBox
        try:
            search_Textbox = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.ID, "search"))
            )
        except:
            driver.refresh()

        nominas.click_Detail_Employee_1()
        nominas.click_Modify_Salary()
        nominas.click_Accept_Modify_Salary()
        nominas.click_Detail_Employee_3()
        nominas.click_Delete_Employee()
        nominas.click_Continuar()
        nominas.click_Uncheckbox()
        nominas.click_Continuar()
        nominas.click_Calcular()
        nominas.click_Delete_Nomina()

        # Creamos el Objeto 'logout' INSTANCIANDO a la Clase MyLogoutPage().
        logout = MyLogoutPage(driver)
        logout.click_Active_User()
        logout.click_Logout()

    @classmethod
    def tearDownClass(cls):
        print("END of TestCase")
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
