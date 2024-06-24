import time
import pytest
from selenium.webdriver.common.by import By

from Pages.Homepage import HomePg
from Pages.ProductPage import ProductPg
from tests.test_setup import TestSetup


class Test_Search((TestSetup)):

    def test_exist_search(self):
        homepgobj = HomePg(self.driver)
        prodpgobj=homepgobj.input_in_seachbar_and_click("iPhone")
        prodpgobj.product_found()

    def test_nonexist_search(self):
        homepgobj = HomePg(self.driver)
        prodpgobj =homepgobj.input_in_seachbar_and_click("Boat")
        prodpgobj.no_product_message()


    def test_empty_search(self):
        homepgobj = HomePg(self.driver)
        prodpgobj = homepgobj.input_in_seachbar_and_click("")
        prodpgobj.no_product_message()

