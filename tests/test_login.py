import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait

from Pages.ContactUsPage import ContactPg
from Pages.Homepage import HomePg
from Pages.LoginPage import LoginPg
from Pages.LoginSuccessPage import LoginSuccessPg
from Pages.RegisterPage import RegPg
from tests.test_setup import TestSetup


class Test_Login(TestSetup):

    def test_login_valid(self):
        homepgobj = HomePg(self.driver)
        regobj= RegPg(self.driver)
        logsobj=LoginSuccessPg(self.driver)
        homepgobj.click_my_account()
        logobj=homepgobj.click_on_loginH()
        regobj.enter_email("laposok736@exeneli.com")
        regobj.enter_pw("abc123")
        logobj.click_on_login()
        logsobj.login_succes_message()

    def test_login_invalid(self):
        homepgobj = HomePg(self.driver)
        regobj = RegPg(self.driver)
        logobj = LoginPg(self.driver)
        homepgobj.click_my_account()
        homepgobj.click_on_loginH()
        regobj.enter_email("laposok736@exeneli.com")
        regobj.enter_pw("abc123e")
        logobj.click_on_login()
        logobj.login_error_message()
