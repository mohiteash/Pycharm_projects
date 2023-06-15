# from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time
from Data import demo_objects

# path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
locat_obj = demo_objects.read_locators()

class DemoFile:

    def __init__(self,driver):
        self.driver = driver

    def demo_camera(self):
        element = self.driver.find_element(*locat_obj['txt_electronics'])
        ac_obj = ActionChains(self.driver)
        ac_obj.move_to_element(element).perform()



        element1 = self.driver.find_element(*locat_obj['txt_camera'])
        ac_obj.click(element1).perform()


        # element2 = self.driver.find_element(*locat_obj['txt_sortby'])
        # sel_obj = Select(element2)
        # sel_obj.select_by_visible_text("Position")

        # ac_obj = ActionChains(self.driver)
        # ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        # time.sleep(2)
        # ac_obj.send_keys(Keys.PAGE_UP)
        # time.sleep(2)
        # sel_obj.select_by_visible_text("Name: A to Z")
        # time.sleep(5)
        # driver.back()
        # ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        # time.sleep(2)
        # ac_obj.send_keys(Keys.PAGE_UP)
        # time.sleep(2)
        # self.driver.back()
        #
        # time.sleep(10)
        #
        # sel_obj.select_by_value("https://demowebshop.tricentis.com/camera-photo?orderby=6")
        # time.sleep(5)
        # # driver.back()
        # ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        # time.sleep(2)
        # ac_obj.send_keys(Keys.PAGE_UP)
        # time.sleep(2)
        # self.driver.back()
        # time.sleep(3)
        #
        # sel_obj.select_by_visible_text("Price: Low to High")
        # time.sleep(5)
        # # driver.back()
        # ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        # time.sleep(2)
        # ac_obj.send_keys(Keys.PAGE_UP)
        # time.sleep(2)
        # self.driver.back()
        #
        # sel_obj.select_by_visible_text("Price: High to Low")
        # time.sleep(5)
        # # driver.back()
        # ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        # time.sleep(2)
        # ac_obj.send_keys(Keys.PAGE_UP)
        # time.sleep(2)
        # self.driver.back()
        # #
        # sel_obj.select_by_visible_text("Created on")
        # time.sleep(5)
        # # driver.back()
        # ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        # time.sleep(2)
        # ac_obj.send_keys(Keys.PAGE_UP)
        # time.sleep(2)
        # self.driver.back()
        rating = self.driver.find_elements("xpath","")


    def cam_dispaly(self):



        element3 = self.driver.find_element(*locat_obj['txt_display'])
        sel_obj = Select(element3)
        sel_obj.select_by_index(0)
        time.sleep(5)
        # driver.back()
        ac_obj = ActionChains(self.driver)
        ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        ac_obj.send_keys(Keys.PAGE_UP)
        time.sleep(2)
        self.driver.back()
        #
        sel_obj.select_by_index(1)
        time.sleep(5)
        # driver.back()
        ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        ac_obj.send_keys(Keys.PAGE_UP)
        time.sleep(2)
        self.driver.back()
        #
        sel_obj.select_by_index(2)
        time.sleep(5)
        # driver.back()
        ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        ac_obj.send_keys(Keys.PAGE_UP)
        time.sleep(2)
        self.driver.back()


    def cam_view(self):
        element4 = self.driver.find_element(*locat_obj['txt_viewby'])
        sel_obj = Select(element4)
        sel_obj.select_by_visible_text("List")
        # time.sleep(5)
        # driver.back()
        ac_obj = ActionChains(self.driver)
        ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        ac_obj.send_keys(Keys.PAGE_UP)
        time.sleep(2)
        # self.driver.back()
        # #
        # sel_obj.select_by_visible_text("Grid")
        # time.sleep(10)
        # # driver.back()
        # ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        # time.sleep(2)
        # ac_obj.send_keys(Keys.PAGE_UP)
        # time.sleep(2)
        # self.driver.back()

        # ele1 = driver.find_element("xpath", "//strong[text()='Filter by price']")
        # ac_obj.move_to_element(ele1).perform()


    def cam_filter(self):
        self.driver.find_element(*locat_obj['txt_price1']).click()
        time.sleep(2)
        ac_obj = ActionChains(self.driver)
        # ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        # time.sleep(2)
        # ac_obj.send_keys(Keys.PAGE_UP)
        # time.sleep(2)
        self.driver.find_element(*locat_obj['txt_price_remove1']).click()
        # time.sleep(2)

        self.driver.find_element(*locat_obj['txt_price2']).click()
        # time.sleep(2)
        # ac_obj.send_keys(Keys.PAGE_DOWN).perform()
        # time.sleep(2)
        # ac_obj.send_keys(Keys.PAGE_UP)
        # time.sleep(2)
        self.driver.find_element(*locat_obj['txt_price_remove2']).click()


    def cam_des(self):
        list1 = ['1MP 60GB Hard Drive Handycam Camcorder', 'Camcorder', 'Digital SLR Camera 12.2 Mpixel',
                 'High Definition 3D Camcorder']
        for element in list1:
            self.driver.find_element("xpath", f"//a[text()='{element}']").click()
            # time.sleep(5)
            self.driver.back()
            # time.sleep(2)

    def cell_sort(self):

        # wait_obj = WebDriverWait(self.driver, 30)
        # wait_obj.until(expected_conditions.presence_of_element_located(("xpath","(//a[@href='/electronics'])[1]")))


        element = self.driver.find_element(*locat_obj['txt_electro'])
        # time.sleep(3)
        ac_obj = ActionChains(self.driver)
        # time.sleep(3)
        ac_obj.move_to_element(element).perform()
        # time.sleep(5)

        element1 = self.driver.find_element(*locat_obj['txt_cell'])
        # time.sleep(3)
        ac_obj.click(element1).perform()
        # time.sleep(5)

        # ac_obj = ActionChains(self.driver)

        element2 = self.driver.find_element(*locat_obj['txt_sortby_cell'])
        sel_obj = Select(element2)
        sel_obj.select_by_visible_text("Position")
        # time.sleep(5)

        sel_obj.select_by_visible_text("Name: A to Z")
        # time.sleep(5)
        self.driver.back()

        # sel_obj.select_by_visible_text("Name: Z to A")
        # time.sleep(5)
        # self.driver.back()
        #
        # sel_obj.select_by_visible_text("Price: Low to High")
        # time.sleep(5)
        # self.driver.back()
        #
        # sel_obj.select_by_visible_text("Price: High to Low")
        # time.sleep(5)
        # self.driver.back()
        #
        # sel_obj.select_by_visible_text("Created on")
        # time.sleep(5)
        # self.driver.back()

    def cell_display(self):
        element3 = self.driver.find_element(*locat_obj['txt_display_cell'])
        sel_obj = Select(element3)
        sel_obj.select_by_index(0)
        # time.sleep(5)
        self.driver.back()

        # sel_obj.select_by_index(1)
        # time.sleep(5)
        # self.driver.back()
        #
        # sel_obj.select_by_index(2)
        # time.sleep(5)
        # self.driver.back()

    def cell_view(self):
        element4 = self.driver.find_element(*locat_obj['txt_viewby_cell'])
        sel_obj = Select(element4)
        sel_obj.select_by_visible_text("List")
        # time.sleep(5)
        self.driver.back()

        # sel_obj.select_by_visible_text("Grid")
        # time.sleep(5)

    def cell_des(self):

        list2 = ['Smartphone', 'Used phone', 'Phone Cover']
        for item in list2:
            self.driver.find_element("xpath", f"//a[text()='{item}']").click()
            # time.sleep(5)
            self.driver.back()
            # time.sleep(2)

    def cell_addto(self):
        self.driver.find_element(*locat_obj['txt_add1']).click()
        # time.sleep(2)
        self.driver.find_element(*locat_obj['txt_add2']).click()
        # time.sleep(2)







# print(locat_obj)
# demo = DemoFile()
# demo.demo_camera()
# demo.cam_dispaly()
# demo.cam_view()
# demo.cam_filter()
# demo.cam_des()
# demo.cell_sort()
# demo.cell_display()
# demo.cell_view()
# demo.cell_des()
# demo.cell_addto()


































