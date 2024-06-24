from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginSuccessPg:

    def __init__(self, driver):
        self.driver = driver

    myacctxt="My Account"
    xmyacctxt = "//h2[normalize-space()='My Account']"



    def login_succes_message(self):
        def login_error_message(self):
            d = self.driver.find_element(By.XPATH, self.xmyacctxt).text.__eq__(self.myacctxt)
            assert d
