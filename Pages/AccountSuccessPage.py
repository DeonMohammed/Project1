from selenium import webdriver
from selenium.webdriver.common.by import By


class AccountSuccessPg:

    def __init__(self,driver):
        self.driver=driver

    accountcreated = "Your Account Has Been Created!"
    xaccountcreated = "//h1[normalize-space()='Your Account Has Been Created!']"


    def account_created_message(self):
        a= self.driver.find_element(By.XPATH,self.xaccountcreated).text.__eq__(self.accountcreated)
        assert a

