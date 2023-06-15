import pytest
from selenium import webdriver
import time
path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get("https:demo.actitime.com/login.do")
driver.maximize_window()
driver.implicitly_wait(30)

@pytest.mark.dependency()
def test_login():
    driver.find_element_by_class_name("textField").send_keys("admin")
    time.sleep(2)
    driver.find_element("name", "pwd").send_keys("manager")
    time.sleep(2)
    driver.find_element("xpath", "//div[text()='Login ']").click()

@pytest.mark.dependency(depends=["test_login"])
def test_logout():
    driver.find_element("xpath", "//a[text()='Logout']").click()




















