import pytest
# from selenium import webdriver
# import time
# path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# #
# driver.get("https:demo.actitime.com/login.do")
# driver.maximize_window()
# driver.implicitly_wait(30)
'''
# @pytest.mark.parametrize("user_,pwd_", [("admin", "manager"),("trainee", "trainee")])
# def test_login(user_,pwd_):
#     driver.find_element_by_class_name("textField").send_keys(user_)
#     time.sleep(2)
#     driver.find_element("name", "pwd").send_keys(pwd_)
#     time.sleep(2)
#     driver.find_element("xpath", "//div[text()='Login ']").click()
#     time.sleep(2)
#     driver.find_element("xpath", "//a[text()='Logout']").click()


# @pytest.mark.parametrize("a, b",[(6,4),(8, 5)])
# def test_add(a,b):
#     res = a*b
#     print(res)
'''

'''
@pytest.mark.parametrize("l", [("admin", "manager"),("trainee", "trainee")])
def test_login(l):
    driver.find_element_by_class_name("textField").send_keys(l[0])
    time.sleep(2)
    driver.find_element("name", "pwd").send_keys(l[1])
    time.sleep(2)
    driver.find_element("xpath", "//div[text()='Login ']").click()
    time.sleep(2)
    driver.find_element("xpath", "//a[text()='Logout']").click()
'''


###########  @pytest.mark.skip(reason=" ")

class TestCalculator:
    a= 6
    b= 2

    @pytest.mark.skip(reason="simply to check")
    def test_add(self):
        assert self.a + self.b == 8,   "invalid output"

    def test_div(self):
        assert self.a/self.b == 3,   "invalid division"



class TestCalculator1:
    a= 6
    b= 2

    @pytest.mark.skipif(b==3,reason="simply to check")
    def test_add1(self):
        assert self.a + self.b == 8,   "invalid output"

    def test_div1(self):
        assert self.a/self.b == 3,   "invalid division"
        print("condition is passed")







