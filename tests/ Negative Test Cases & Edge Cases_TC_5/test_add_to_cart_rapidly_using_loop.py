import logging
import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")

class Test_add_to_cart_rapidly_using_loop:

    def test_add_to_cart_rapidly_using_loop_1(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)

        for i in range(1,51):
            home_page.add_backpack_to_cart()
            home_page.get_homepage_cart_icon_click()
            self.driver.back()

            try:
                home_page.remove_backpack_from_cart()
            except:
                log.error(f"⚠️ Remove button not found in round {i}")

            current_url = self.driver.current_url
            expected_url = "https://www.saucedemo.com/inventory.html"

            assert current_url == expected_url, f"❌ URL Expected: {expected_url}, but got: {current_url}"

