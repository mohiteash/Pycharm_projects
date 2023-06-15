# To do lower level operations will be using ActionChains
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium .webdriver.common.keys import Keys
path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
'''
driver.get("https://www.meesho.com/")
driver.maximize_window()

women_ethnic= driver.find_element("xpath", "//span[text()='Women Ethnic']")

ac_obj = ActionChains(driver)
# ac_obj.move_to_element(women_ethnic).perform()

ac_obj.double_click(women_ethnic).perform()
'''

driver.get("file:///D:/Selenium_library/demo%20(1).html")
driver.maximize_window()

ele_dd = driver.find_element("xpath", "//button[@ondblclick='dbl()']")
###double click
ac_obj = ActionChains(driver)
ac_obj.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
ac_obj.double_click(ele_dd).perform()
time.sleep(2)
ac_obj.send_keys(Keys.PAGE_UP).perform()

####simulating keys

ac_obj.key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform()















