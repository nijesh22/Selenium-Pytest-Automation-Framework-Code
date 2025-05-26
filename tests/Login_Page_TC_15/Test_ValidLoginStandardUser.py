import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup")
class Test_validlogin():
    def test_loginisvalid(self):
        #login using valid standard user
        wait = WebDriverWait(self.driver, 10)
        lp = LoginPage(self.driver, wait)
        lp.swag_labs_loginIsvalid("Nijesh")