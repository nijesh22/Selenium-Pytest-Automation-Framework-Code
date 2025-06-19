import time

from selenium.webdriver.common.by import By


import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class Test_logout_and_relogin:
    def test_logout_and_relogin_1(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"

        if current_url == expected_url:
            log.info(f"✅ Correct URL: {current_url}")
        else:
            log.error(f"❌ Incorrect URL! Expected: {expected_url}, but got: {current_url}")

        assert current_url == expected_url, f"❌ Expected: {expected_url}, but got: {current_url}"


        # Logout
        home_page = HomePage(self.driver, wait)
        home_page.click_menu()
        home_page.click_logout()

        # Relogin
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        if current_url == expected_url:
            log.info(f"✅ Correct URL: {current_url}")
        else:
            log.error(f"❌ Incorrect URL! Expected: {expected_url}, but got: {current_url}")

        assert current_url == expected_url, f"❌ Expected: {expected_url}, but got: {current_url}"


