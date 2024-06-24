import pytest
from selenium import webdriver

from utilities import read_from_config


@pytest.fixture()
def initiate(request):
    browser=read_from_config.readconfig("INFO","browser")
    driver=None
    if browser.__eq__("Chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("Firefox") :
        driver=webdriver.Firefox()
    url=read_from_config.readconfig("INFO","URL")
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
