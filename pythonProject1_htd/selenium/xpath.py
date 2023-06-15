from selenium import webdriver
import time

path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"

driver_obj = webdriver.Chrome(path)


# driver_obj.get("https://demowebshop.tricentis.com/")
# driver_obj.get("https://demowebshop.tricentis.com/books")
# time.sleep(2)
# driver_obj.maximize_window()
# time.sleep(2)

################################################################################
# books = ['Computing and Internet','Copy of Computing and Internet EX', 'Fiction','Fiction EX','Health Book', 'Science']
####driver_obj.find_element('xpath',"//input[@value='Add to cart']").click()
# for book in books[::2]:
#     driver_obj.find_element('xpath',f"//a[text()='{book}']/../..//input[@value='Add to cart']").click()
#     time.sleep(2)

# books=['Computing and Internet', 'Fiction', 'Health Book']
# for book in books:
#     driver_obj.find_element("xpath", f"//a[text()='{book}']/../../../..//input[@value='Add to cart']").click()
#     time.sleep(2)
###############################################################################################
'''Que.2'''

# driver_obj.find_element("xpath","//label[text()='Excellent']/../..//input[@type='radio']").click()
# time.sleep(2)
# driver_obj.find_element("xpath", "//input[@value='Vote']").click()
# time.sleep(2)


'''Q3'''
# driver_obj.get("https://services.smartbear.com/samples/testcomplete14/smartstore/sunglasses")
# time.sleep(2)
# driver_obj.maximize_window()

'''Q8'''
# driver_obj.get("file:///C:/Users/Mohite's/Downloads/demo%20(1).html")
# list1=['Ruby', 'Java', 'Perl', 'Python', 'C#', 'JavaScript']
# for element in list1[::-1]:
#     driver_obj.find_element("xpath",f"//td[text()='{element}']/..//input[@name='download']").click()
#     time.sleep(2)

'''Q9'''
# driver_obj.get("file:///C:/Users/Mohite's/Downloads/demo%20(1).html")
# list1=['Ruby', 'Java', 'Perl', 'Python', 'C#', 'JavaScript']
# for element in list1[::2]:
#     driver_obj.find_element("xpath",f"//td[text()='{element}']/..//input[@name='download']").click()
#     time.sleep(2)


'''Q10'''
# driver_obj.get("file:///C:/Users/Mohite's/Downloads/demo%20(1).html")
# list1=['Ruby', 'Java', 'Perl', 'Python', 'C#', 'JavaScript']
# index = 0
# while index < len(list1):
#     if index == 0 :
#         driver_obj.find_element("xpath",f"//td[text()='{list1[index]}']/..//input[@name='download']").click()
#         time.sleep(2)
#     elif index == len(list1)-1:
#         driver_obj.find_element("xpath", f"//td[text()='{list1[index]}']/..//input[@name='download']").click()
#         time.sleep(2)
#     index += 1


































