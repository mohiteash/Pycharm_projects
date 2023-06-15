# Explicit wait


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait      #Explicit_Wait class
from selenium.webdriver.support import expected_conditions

path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(path)

# driver.get("file:///C:/Users/Mohite's/Downloads/progressbar%20(1).html")
# driver.maximize_window()
# driver.find_element("xpath", "//button[text()='Click Me']").click()
# wait_obj= WebDriverWait(driver,30)    #WebDriverWait to give explicit time
# wait_obj.until(expected_conditions.presence_of_element_located(("xpath","//div[text()='100%']")))
# driver.find_element("xpath", "//button[text()='Click Me']").click()

###### create a function which should check both visibility, enable

driver.get("file:///C:/Users/Mohite's/Downloads/demo%20(1).html")
driver.maximize_window()
ele = driver.find_element("id","first_name")
# print(ele.is_enabled())
# print(ele.is_displayed())

# def is_visible_enabled(locator):












