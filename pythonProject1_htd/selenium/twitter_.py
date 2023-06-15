from selenium import webdriver
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

#######################################################
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()

####################################################
# ac_obj= ActionChains(driver)
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# driver.find_element("xpath", "//a[text()='Twitter']").click()
# time.sleep(2)
# handle = driver.window_handles
# print(handle)
# driver.switch_to.window(handle[1])
# driver.find_element("xpath", "//span[text()='Follow']").click()
#################################################################
'''

driver.find_element("xpath", "//input[@value='Search']").click()
time.sleep(2)
## Javascript popup
## switch to the alert
alert_obj = driver.switch_to.alert

## accept it or dismiss # alert_obj.accept() ---- ok,accept, alert_obj.dismiss() --- cancel, dismiss
alert_obj.accept()

driver.find_element_by_link_text("Log in").click()
'''
#####################################################################################
'''
driver.get("file:///D:/Selenium_library/demo%20(1).html")
driver.maximize_window()
driver.find_element("xpath", "//button[text()='Delete']").click()

# switch to alert
time.sleep(2)
alert_obj = driver.switch_to.alert
time.sleep(2)
alert_obj.dismiss()


### File upload popup
file_path = r"D:\Documents"
driver.find_element("xpath", "//input[@id='resume']").send_keys(file_path)



'''
##################################################################

'''
@given(u'launch the browser')
def step_impl(context):
    path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
    context.driver = webdriver.Chrome(executable_path=path)



@when(u'open demo web shop home page')
def step_impl(context):
    context.driver.get("https://demowebshop.tricentis.com/")
    context.driver.maximize_window()



@when('click on Electronics category')
def step_impl(context):
    context.driver.find_element("xpath", "//a[@href='/electronics']").click()



@when('Click on camera')
def step_impl(context):
    context.driver.find_element("xpath", "(//div[@class='sub-category-item'])[1]").click()



@when('Click on sort by dropdown, click on "Name: A to Z"')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element("xpath", "//select[@id='products-orderby']").click()
    context.driver.find_element("xpath", "//select[@id='products-orderby']//option[text()='Name: A to Z']").click()





@then('verify products are arranged by selected position')
def step_impl(context):
    assert True, "Test passed"

'''






















