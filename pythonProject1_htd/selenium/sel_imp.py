#Implicit wait - it is applied only to find_element, find_elements
#              - you cannot give the condition

from selenium import webdriver
path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(path)

# driver.implicitly_wait(30)

# driver.get("file:///C:/Users/Mohite's/Downloads/loading%20(1).html")
# driver.maximize_window()
# start = time.time()
# driver.find_element_by_name("fname").send_keys("Ash")
# end = time.time()

driver.get("file:///C:/Users/Mohite's/Downloads/progressbar%20(1).html")
driver.maximize_window()
driver.find_element("xpath", "//button[text()='Click Me']").click()
driver.find_element("xpath", "//div[text()='100%']")
driver.find_element("xpath", "//button[text()='Click Me']").click()

























