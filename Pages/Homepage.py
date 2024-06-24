from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPg
from Pages.ProductPage import ProductPg


class HomePg:

    def __init__(self, driver):
        self.driver = driver

    xmyaccount = "//span[normalize-space()='My Account']"
    xregister = "//a[normalize-space()='Register']"
    xlogin = "//a[normalize-space()='Login']"
    xcontact = "//ul[@class='list-unstyled']//a[normalize-space()='Contact Us']"
    xmyacc = "//h2[normalize-space()='My Account']"
    xsearchbar = "//input[@placeholder='Search']"
    xsearchbutton = "//i[@class='fa fa-search']"

    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.xmyaccount).click()

    def click_register(self):
        self.driver.find_element(By.XPATH, self.xregister).click()

    def click_on_contactus(self):
        self.driver.find_element(By.XPATH, self.xcontact).click()

    def click_on_myaccount(self):
        self.driver.find_element(By.XPATH, self.xmyacc).click()

    def input_in_seachbar_and_click(self,product):
        self.driver.find_element(By.XPATH, self.xsearchbar).send_keys(product)
        self.click_on_searchbutton()
        return ProductPg(self.driver)

    def click_on_searchbutton(self):
        self.driver.find_element(By.XPATH, self.xsearchbutton).click()


    def click_on_loginH(self):
        self.driver.find_element(By.XPATH, self.xlogin).click()
        return LoginPg(self.driver)
