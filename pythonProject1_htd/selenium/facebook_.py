from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"

driver_obj = webdriver.Chrome(path)
driver_obj.get("https://www.facebook.com/reg/")

driver_obj.find_element("xpath", "//input[@name='firstname']").send_keys('asura')
driver_obj.find_element("xpath", "//input[@name='lastname']").send_keys('dragon')
driver_obj.find_element("xpath", "//input[@name='reg_email__']").send_keys('asuradragon123@gmail.com')
driver_obj.find_element("xpath","//input[@name='reg_email_confirmation__']").send_keys('asuradragon123@gmail.com')
driver_obj.find_element("xpath", "//input[@name='reg_passwd__']").send_keys('Asuradragon#12')

element = driver_obj.find_element("xpath", "//select[@name='birthday_day']")
select_obj = Select(element)
time.sleep(1)
select_obj.select_by_value('14')

element = driver_obj.find_element("xpath", "//select[@name='birthday_month']")
select_obj = Select(element)
time.sleep(1)
select_obj.select_by_visible_text('Dec')

element = driver_obj.find_element("xpath", "//select[@name='birthday_year']")
select_obj = Select(element)
time.sleep(1)
select_obj.select_by_value('2001')

driver_obj.find_element("xpath", "//label[text()='Female']/..//input[@type='radio']").click()
driver_obj.find_element("xpath", "//button[@name='websubmit']").click()


























