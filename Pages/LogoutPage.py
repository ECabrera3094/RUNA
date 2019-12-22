import time

from Locators.Locators import MyLocators

class MyLogoutPage():

    def __init__(self, driver):
        self.driver = driver
        self.XPath_Active_User = MyLocators.XPath_Active_User
        self.CSS_Logout = MyLocators.CSS_Logout

    def click_Active_User(self):
        link_Active_User = self.driver.find_element_by_xpath(self.XPath_Active_User).click()
        time.sleep(0.5)

    def click_Logout(self):
        link_Logout = self.driver.find_element_by_css_selector(self.CSS_Logout).click()
        time.sleep(0.5)
