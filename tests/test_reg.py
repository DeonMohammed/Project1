import time
import secrets

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Pages.AccountSuccessPage import AccountSuccessPg
from Pages.Homepage import HomePg
from Pages.RegisterPage import RegPg
from tests.test_setup import TestSetup


class Test_Reg((TestSetup)):

    def test_register(self):
        homepgobj = HomePg(self.driver)
        regobj = RegPg(self.driver)
        acsuccessobj=AccountSuccessPg(self.driver)
        homepgobj.click_my_account()
        homepgobj.click_register()
        regobj.enter_fname("John")
        regobj.enter_lname("Doe")
        regobj.enter_email(self.email_gen())
        regobj.enter_phone("43567654")
        regobj.enter_pw("ABC123")
        regobj.enter_confirmpw("ABC123")
        regobj.click_agree()
        regobj.click_continue()
        acsuccessobj.account_created_message()



    def test_not_agree(self):
        homepgobj = HomePg(self.driver)
        regobj = RegPg(self.driver)
        acsuccessobj = AccountSuccessPg(self.driver)
        homepgobj.click_my_account()
        homepgobj.click_register()
        regobj.enter_fname("John")
        regobj.enter_lname("Doe")
        regobj.enter_email(self.email_gen())
        regobj.enter_phone("43567654")
        regobj.enter_pw("ABC123")
        regobj.enter_confirmpw("ABC123")
        # regobj.click_agree()
        regobj.click_continue()
        regobj.validate_privacy()

    def email_gen(self):
        return f"{secrets.token_hex(2)}@gmail.com"
