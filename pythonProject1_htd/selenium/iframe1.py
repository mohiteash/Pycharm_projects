from selenium import webdriver
import time

path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get("file:///C:/Users/Mohite's/Downloads/iframe%20(1).html")
driver.maximize_window()

driver.switch_to.frame(0)
driver.find_element_by_id("small-searchterms").send_keys('books')
time.sleep(2)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(2)
driver.switch_to.default_content()
time.sleep(2)
driver.switch_to.frame("FR2")
time.sleep(2)
driver.find_element("xpath", "//input[@id='search_form']").send_keys('vehicle')
time.sleep(2)
driver.find_element("xpath", "//button[@type='submit']").click()












