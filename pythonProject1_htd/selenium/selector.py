from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("file:///C:/Users/Mohite's/Downloads/demo%20(1).html")
driver.maximize_window()
time.sleep(2)

'''
ele = driver.find_element_by_id("standard_cars")
sel_obj = Select(ele)
time.sleep(2)
sel_obj.select_by_visible_text("Audi")
time.sleep(2)
sel_obj.select_by_value("bmw")
time.sleep(2)
sel_obj.select_by_index(4)
time.sleep(2)


####getting all the options in select box
all_options = sel_obj.options
print(all_options)
for option in all_options:
    sel_obj.select_by_visible_text(option.text)
    time.sleep(1)


for index in range(len(all_options)):
    sel_obj.select_by_index(index)
    time.sleep(1)
    
for index,value in enumerate(all_options):
    sel_obj.select_by_index(index)
    time.sleep(1)
'''

#handling multiple select in list
ele = driver.find_element("id", "multiple_cars")
obj_ms = Select(ele)
obj_ms.select_by_visible_text("Audi")
time.sleep(1)
obj_ms.select_by_visible_text("Ford")
time.sleep(1)
obj_ms.select_by_visible_text("BMW")
time.sleep(1)
obj_ms.select_by_index(5)
print(obj_ms.is_multiple)

# option = obj_ms.options

# sel_option = obj_ms.all_selected_options


## to get only selected item
option = obj_ms.all_selected_options
for item in option:
    print(item.text)

#to get the first element that is selected
print(obj_ms.first_selected_option.text)


obj_ms.deselect_by_index(1)































