import time

import pytest
from selenium.webdriver.common.devtools.v134.profiler import start
from selenium.webdriver.support.wait import WebDriverWait

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestRefreshMaintainsLoginState:
    def test_refresh_maintains_login_state(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        for i in range(1 ,11):
            self.driver.refresh()
            current_url = self.driver.current_url
            expected_url = "https://www.saucedemo.com/inventory.html"

            assert current_url == expected_url, f"❌ URL Expected: {expected_url}, but got: {current_url}"
            log.info(f"sucessfully refreshed round : {i}")