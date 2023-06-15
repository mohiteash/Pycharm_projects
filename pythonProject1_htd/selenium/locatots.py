from selenium import webdriver
import time

path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"

driver_obj = webdriver.Chrome(path)


# driver_obj.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# driver_obj.maximize_window()
# time.sleep(2)
# driver_obj.minimize_window()
# time.sleep(2)
# driver_obj.maximize_window()
# time.sleep(2)
# driver_obj.refresh()
# print(driver_obj.title)
# print(driver_obj.current_url)
# # driver_obj.close()
# driver_obj.quit()

#id locator
# driver_obj.find_element_by_id("small-searchterms").send_keys("books")

#name locator
# driver_obj.find_element_by_name("q").send_keys("books")
#
#class name locator
# driver_obj.find_element_by_class_name("search-box-text ui-autocomplete-input").click()
#
#link text locator
# driver_obj.find_element_by_link_text("Electronics").click()

#partial link text locator
# driver_obj.find_element_by_partial_link_text("Ele").click()

#css selector
# driver_obj.find_element_by_css_selector('input[value="Search store"]')

#tag name
# links = driver_obj.find_elements_by_tag_name("a")
# # print(links)
# for lin in links:
#     print(lin.text)

############################################################################
#####10/11/2022#########

# driver_obj.find_element('xpath','//a[@class="ico-register"]').click()

'''xpath'''

# driver_obj.find_element('xpath','//a[text()="Register"]').click()

###"https:demo.actitime.com/login.do"
















