import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestValidateResponsiveLayout(BaseTest):
    def test_validate_responsive_layout(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        # wait = WebDriverWait(self.driver, 10)
        # login_page = LoginPage(self.driver, wait)
        # login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        # login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)

        # Resize to mobile
        home_page.resize_window(375, 667)
        time.sleep(1)

        assert home_page.is_burger_menu_visible(), "❌ Burger menu not visible!"

        home_page.click_menu()
        home_page.side_menu_close_button()

        # Resize to desktop
        home_page.resize_window(1366, 768)
        time.sleep(1)
        assert home_page.is_burger_menu_visible(), "❌ Burger menu not visible!"

        home_page.click_menu()
        home_page.side_menu_close_button()

        # Resize to tablet
        self.driver.set_window_size(768, 1024)
        time.sleep(1)
        assert home_page.is_burger_menu_visible(), "❌ Burger menu not visible!"

        home_page.click_menu()
        home_page.side_menu_close_button()