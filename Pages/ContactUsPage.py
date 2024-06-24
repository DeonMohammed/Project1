from selenium import webdriver
from selenium.webdriver.common.by import By


class ContactPg:

    def __init__(self,driver):
        self.driver=driver

    contacttxt = "Contact Us"
    xcontacttxt = "//ul[@class='list-unstyled']//a[normalize-space()='Contact Us']"

    def validate_contactus(self):
        b= self.driver.find_element(By.XPATH,self.xcontacttxt).text.__eq__(self.contacttxt)
        assert b