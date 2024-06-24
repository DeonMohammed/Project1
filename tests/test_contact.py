import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Pages.ContactUsPage import ContactPg
from Pages.Homepage import HomePg
from tests.test_setup import TestSetup


class Test_Contact(TestSetup):
    global driver

    def test_ContactHome(self):
        homepgobj = HomePg(self.driver)
        contactusobj = ContactPg(self.driver)
        homepgobj.click_on_contactus()
        contactusobj.validate_contactus()

    def test_ContactReg(self):
        homepgobj = HomePg(self.driver)
        contactusobj = ContactPg(self.driver)
        homepgobj.click_my_account()
        homepgobj.click_register()
        homepgobj.click_on_contactus()
        contactusobj.validate_contactus()

    def test_ContactLogin(self):
        homepgobj = HomePg(self.driver)
        contactusobj = ContactPg(self.driver)
        homepgobj.click_my_account()
        homepgobj.click_on_loginH()
        homepgobj.click_on_contactus()
        contactusobj.validate_contactus()

