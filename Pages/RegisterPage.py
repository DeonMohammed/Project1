from selenium import webdriver
from selenium.webdriver.common.by import By


class RegPg:

    def __init__(self,driver):
        self.driver=driver

    xfname = "//input[@id='input-firstname']"
    xlname = "//input[@id='input-lastname']"
    xemail = "//input[@id='input-email']"
    xphone = "//input[@id='input-telephone']"
    xpw = "//input[@id='input-password']"
    xconfirmpw = "//input[@id='input-confirm']"
    xagree = "//input[@name='agree']"
    xcontinue = "//input[@value='Continue']"
    privypol = "Warning: You must agree to the Privacy Policy!"
    xprivypol = "//div[@class='alert alert-danger alert-dismissible']"


    def enter_fname(self,fname):
        self.driver.find_element(By.XPATH, self.xfname).send_keys(fname)

    def enter_lname(self,lname):
        self.driver.find_element(By.XPATH, self.xlname).send_keys(lname)

    def enter_email(self,email):
        self.driver.find_element(By.XPATH, self.xemail).send_keys(email)

    def enter_phone(self,phone):
        self.driver.find_element(By.XPATH, self.xphone).send_keys(phone)

    def enter_pw(self, pw):
        self.driver.find_element(By.XPATH, self.xpw).send_keys(pw)


    def enter_confirmpw(self,confirmpw):
        self.driver.find_element(By.XPATH, self.xconfirmpw).send_keys(confirmpw)



    def click_agree(self):
        self.driver.find_element(By.XPATH, self.xagree).click()

    def click_continue(self):
        self.driver.find_element(By.XPATH, self.xcontinue).click()



    def validate_privacy(self):
        g = self.driver.find_element(By.XPATH, self.xprivypol).text.__eq__(self.privypol)
        assert g