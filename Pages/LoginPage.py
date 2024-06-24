from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPg:

    def __init__(self,driver):
        self.driver=driver

    xloginbutton = "//input[@value='Login']"
    wronglogin = "Warning: No match for E-Mail Address and/or Password."
    xwronglogin = "//div[@class='alert alert-danger alert-dismissible']"



    def click_on_login(self):
        self.driver.find_element(By.XPATH, self.xloginbutton).click()

    def login_error_message(self):
        c= self.driver.find_element(By.XPATH,self.xwronglogin).text.__eq__(self.wronglogin)
        assert c
