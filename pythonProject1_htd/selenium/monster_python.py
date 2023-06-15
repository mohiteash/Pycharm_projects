from selenium import webdriver
import time

path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get("https://www.monsterindia.com/")
driver.maximize_window()

driver.find_element_by_id("SE_home_autocomplete").send_keys("python")
time.sleep(2)
driver.find_element("xpath", "//input[@class='btn']").click()
time.sleep(2)
driver.find_element("xpath", "//p[@class='text']").click()
time.sleep(2)
handle = driver.window_handles
print(handle)
driver.switch_to.window(handle[1])
driver.find_element("xpath", "//input[@type='text']").send_keys('9657224701')
time.sleep(2)
driver.find_element("xpath", "//input[@type='password']").send_keys('abcd@123')
time.sleep(2)
driver.find_element("xpath", "//input[@type='submit']").click()








