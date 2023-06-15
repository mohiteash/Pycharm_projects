import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium .webdriver.common.keys import Keys

path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get("https://www.monsterindia.com/")

element = driver.find_element("xpath","//a[@data-check='menutab']")
ac_obj= ActionChains(driver)
ac_obj.move_to_element(element).perform()
time.sleep(2)

element = driver.find_element("xpath","//a[text()='Jobs by Skills']")
# ac_obj= ActionChains(driver)
ac_obj.move_to_element(element).perform()
time.sleep(2)

element = driver.find_element("xpath", "//a[@href='https://www.monsterindia.com/search/python-jobs']")
# ac_obj= ActionChains(driver)
ac_obj.click(element).perform()




