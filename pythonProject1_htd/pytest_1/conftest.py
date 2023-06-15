import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium .webdriver.common.keys import Keys
import time

path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
@pytest.fixture()
def _driver():
    driver = webdriver.Chrome(executable_path=path)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver
    print(driver.title)
    driver.close()










