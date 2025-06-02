import time
from operator import truediv

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.LoginPage import LoginPage
from conftest import driver


@pytest.mark.usefixtures("setup")
class Test_validlogin():
    def test_loginisvalid(self):
        #login using valid standard user
        wait = WebDriverWait(self.driver, 10)
        standard_user = LoginPage(self.driver, wait)
        standard_user.swag_labs_loginIsvalid("standard_user","secret_sauce")
        standard_user.swag_labs_login_button()

        URL = self.driver.current_url
        expected_url = 'https://www.saucedemo.com/inventory.html'

        print(f"Current URL is: {URL}")

        # Assert to validate correctness
        assert URL == expected_url, f"URL is different! Expected: {expected_url}, but got: {URL}"

        print("✅ URL is correct.")










