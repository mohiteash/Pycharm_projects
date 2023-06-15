from selenium import webdriver
import time

path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"

driver_obj = webdriver.Chrome(path)

driver_obj.get("https:demo.actitime.com/login.do")
time.sleep(2)
driver_obj.maximize_window()
time.sleep(2)
# driver_obj.find_element_by_id("username").send_keys("admin")
# driver_obj.find_element_by_name("pwd").send_keys("manager")
# driver_obj.find_element_by_id("loginButton").click()
# time.sleep(2)
# driver_obj.find_element_by_class_name("logout").click()

# driver_obj.find_element('xpath','//input[@class="textField"]').send_keys("admin")
# driver_obj.find_element_by_css_selector('input[type="password"]').send_keys('manager')
# driver_obj.find_element_by_link_text('Login').click()
# time.sleep(2)
# driver_obj.find_element_by_id('logoutLink').click()

driver_obj.find_element('xpath','(//a[contains(@class, "ico")])[2]')















