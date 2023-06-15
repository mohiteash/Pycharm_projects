from selenium import webdriver
import time

path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

# driver.get("file:///C:/Users/Mohite's/Downloads/demo%20(1).html")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element("xpath","//td[text()='Ruby']/..//input[@name='download']").click()
# driver.find_element("xpath","//td[text()='Java']/..//input[@name='download']").click()

# list1=['Ruby', 'Java', 'Perl', 'Python', 'C#', 'JavaScript']

# for item in list1:
#     xpath_value= f"//td[text()='{item}']/..//input[@name='download']"
#     driver.find_element("xpath", xpath_value).click()


# for item in list1[::-1]:
#     xpath_value= f"//td[text()='{item}']/..//input[@name='download']"
#     driver.find_element("xpath", xpath_value).click()


# driver.get("file:///C:/Users/Mohite's/Downloads/demo%20(1).html")
# driver.maximize_window()
# time.sleep(2)
# list_web_ele = driver.find_elements("xpath","(//tbody)[2]//input")
# print(list_web_ele)
# for element in list_web_ele:
#     element.click()
#     time.sleep(2)
    # driver.back()
'''
list_web_ele = driver.find_elements("xpath", "//input[@name='fname']")
# list_web_ele = driver.find_elements("xpath","//input[contains(@style, 'width: 202px;')]")
list1=['Ruby', 'Python', 'Java', 'Perl', 'C#', 'Javascript', 'PHP', 'C++', 'C']
for element,item in zip(list_web_ele,list1):
    element.send_keys(item)
    time.sleep(2)
'''

####in multiple elements of demo.html

# driver.get("https://www.python.org/")
# driver.maximize_window()
# time.sleep(2)
# links = driver.find_elements("xpath", "//a")
# link_text = []
# for link in links:
#     text_ = link.text
#     print(link.get_attribute("href"))
#
#     if text_:
#         link_text.append(text_)
# print(link_text)
# print(len(link_text))





















