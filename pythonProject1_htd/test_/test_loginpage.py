from POM.login_page import Loginpage


class TestLoginPage:
    def test_login(self,_driver):
        lp = Loginpage(_driver)
        lp.enter_username()
        lp.enter_pwd()
        lp.click_login()



