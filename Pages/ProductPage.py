from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductPg:

    def __init__(self,driver):
        self.driver=driver

    xproductfound = "//a[normalize-space()='iPhone']"
    noprdcttxt = "There is no product that matches the search criteria."
    xnoprdcttxt = "//p[contains(text(),'There is no product that matches the search criter')]"

    def product_found(self):
        def login_error_message(self):
            e = self.driver.find_element(By.XPATH, self.xproductfound).text.__eq__(self.xproductfound)
            assert e

    def no_product_message(self):
        f = self.driver.find_element(By.XPATH, self.xnoprdcttxt).text.__eq__(self.noprdcttxt)
        assert f