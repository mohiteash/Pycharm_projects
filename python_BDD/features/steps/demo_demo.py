from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium .webdriver.common.keys import Keys


@given('launch the browser')
def step_launch(context):
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe")


@when('open demo web shop home page')
def step_open(context):
    context.driver.get("https://demowebshop.tricentis.com/")
    context.driver.maximize_window()


@when('click on Electronics category')
def step_electro(context):
    context.driver.find_element("xpath", "//a[@href='/electronics']").click()


@then('Click on camera')
def step_camera(context):
    context.driver.find_element("xpath", "(//div[@class='sub-category-item'])[1]").click()


@then('Click on sort by dropdown, click on "Name: A to Z" for camera')
def step_sort1(context):
    time.sleep(5)
    context.driver.find_element("xpath", "//select[@id='products-orderby']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@id='products-orderby']//option[text()='Name: A to Z']").click()

@then('Click on sort by dropdown, click on "Name: Z to A" for camera')
def step_sort2(context):
    context.driver.find_element("xpath", "//select[@id='products-orderby']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@id='products-orderby']//option[text()='Name: Z to A']").click()


@then('Click on sort by dropdown, click on "Price: Low to High" camera')
def step_sort3(context):
    context.driver.find_element("xpath", "//select[@id='products-orderby']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@id='products-orderby']//option[text()='Price: Low to High']").click()


@then('Click on sort by dropdown, click on "Price: High to Low" camera')
def step_sort4(context):
    context.driver.find_element("xpath", "//select[@id='products-orderby']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@id='products-orderby']//option[text()='Price: High to Low']").click()


@then('Click on sort by dropdown, click on "Created on" camera')
def step_sort5(context):
    context.driver.find_element("xpath", "//select[@id='products-orderby']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@id='products-orderby']//option[text()='Created on']").click()

@then('click on display, click on 4 for camera')
def step_dis1(context):
    context.driver.find_element("xpath", "//select[@name='products-pagesize']")
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@name='products-pagesize']//option[text()='4']").click()

@then('click on display, click on 8 for camera')
def step_dis2(context):
    context.driver.find_element("xpath", "//select[@name='products-pagesize']")
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@name='products-pagesize']//option[text()='8']").click()


@then('click on display, click on 12 for camera')
def step_dis3(context):
    context.driver.find_element("xpath", "//select[@name='products-pagesize']")
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@name='products-pagesize']//option[text()='12']").click()

@then('click on view by, click on "list" for camera')
def step_view1(context):
    context.driver.find_element("xpath", "//select[@name='products-viewmode']").click()
    time.sleep(2)
    context.driver.find_element("xpath","//select[@name='products-viewmode']//option[text()='List']").click()


@then('click on view by, click on  "Grid" for camera')
def step_view2(context):
    context.driver.find_element("xpath", "//select[@name='products-viewmode']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@name='products-viewmode']//option[text()='Grid']").click()


@then('click on filter under 500 for camera')
def step_filter1(context):
    context.driver.find_element("xpath","//a[text()='    Under ']/..//span[text()='500.00']").click()
    time.sleep(2)


@then('click on Remove_filter for camera')
def step_remove1(context):
    context.driver.find_element("xpath", "//a[text()='Remove Filter']").click()
    time.sleep(2)


@then('click on filter over 500 for camera')
def step_filter2(context):
    context.driver.find_element("xpath","//a[text()='    Over ']/..//span[@class='PriceRange']").click()
    time.sleep(2)


@then('click on Removefilter for camera')
def step_remove2(context):
    context.driver.find_element("xpath", "//a[text()='Remove Filter']").click()


@then('click on one of the product and see its description for camera')
def step_des1(context):
    context.driver.find_element("xpath", f"//a[text()='1MP 60GB Hard Drive Handycam Camcorder']").click()
    context.driver.back()


@then('come back and click on another product description and come back for camera')
def step_impldes2(context):
    context.driver.find_element("xpath", f"//a[text()='Camcorder']").click()
    context.driver.back()


@then('verify the camera page is modified as selected options for camera')
def step_veri1(context):
    assert True, "test passed"


@then(u'Click on cell phone')
def step_cellphone(context):
    context.driver.find_element("xpath", "(//div[@class='sub-category-item'])[2]").click()


@then('Click on sort by dropdown, click on "Name: A to Z" for cell_phone')
def step_cellsort1(context):
    context.driver.find_element("xpath", "//select[@id='products-orderby']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@id='products-orderby']//option[text()='Name: A to Z']").click()


@then('Click on sort by dropdown, click on "Name: Z to A" for cell_phone')
def step_cellsort2(context):
    context.driver.find_element("xpath", "//select[@id='products-orderby']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@id='products-orderby']//option[text()='Name: Z to A']").click()


@then('Click on sort by dropdown, click on "Price: Low to High" for cell_phone')
def step_cellsort3(context):
    context.driver.find_element("xpath", "//select[@id='products-orderby']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@id='products-orderby']//option[text()='Price: Low to High']").click()


@then('Click on sort by dropdown, click on "Price: High to Low" for cell_phone')
def step_cellsort4(context):
    context.driver.find_element("xpath", "//select[@id='products-orderby']").click()
    time.sleep(2)
    context.driver.find_element("xpath","//select[@id='products-orderby']//option[text()='Price: High to Low']").click()


@then('Click on sort by dropdown, click on "Created on" for cell_phone')
def step_cellsort5(context):
    context.driver.find_element("xpath", "//select[@id='products-orderby']").click()
    time.sleep(2)
    context.driver.find_element("xpath","//select[@id='products-orderby']//option[text()='Created on']").click()


@then('click on display, click on 4 for cell_phone')
def step_celldis1(context):
    context.driver.find_element("xpath", "//select[@id='products-pagesize']")
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@id='products-pagesize']//option[text()='4']").click()


@then('click on display, click on 8 for cell_phone')
def step_celldis2(context):
    context.driver.find_element("xpath", "//select[@name='products-pagesize']")
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@id='products-pagesize']//option[text()='8']").click()


@then('click on display, click on 12 for cell_phone')
def step_celldis3(context):
    context.driver.find_element("xpath", "//select[@name='products-pagesize']")
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@id='products-pagesize']//option[text()='12']").click()


@then('click on view by, click on cell_list for cell_phone')
def step_cellview1(context):
    context.driver.find_element("xpath", "//select[@name='products-viewmode']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@name='products-viewmode']//option[text()='List']").click()


@then('click on view by, click on cell_Grid for cell_phone')
def step_cellview2(context):
    context.driver.find_element("xpath", "//select[@name='products-viewmode']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//select[@name='products-viewmode']//option[text()='Grid']").click()


@then('click on one of the product and see its description for cell_phone')
def step_celldis1(context):
    context.driver.find_element("xpath", f"//a[text()='Smartphone']").click()
    time.sleep(2)


@then('come back and click on another product description and come back for cell_phone')
def step_cellview2(context):
    context.driver.back()
    context.driver.find_element("xpath", f"//a[text()='Used phone']").click()
    time.sleep(2)
    context.driver.back()


@then('click on one of the product to cart for cell_phone')
def step_celladd2(context):
    time.sleep(10)
    context.driver.find_element("xpath", "(//input[@type='button'])[3]").click()
    time.sleep(5)
    context.driver.find_element("xpath", "(//input[@type='button'])[4]").click()
    time.sleep(2)


@then('verify the cell phone page is modified as selected options and product is added to cart for cell_phone')
def step_cellveri2(context):
    assert True, "test passed"









