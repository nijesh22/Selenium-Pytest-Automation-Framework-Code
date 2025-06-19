import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProductDetailPage import ProductDetailPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class Test_product_detail_navigation_with_image:
    def test_product_detail_navigation_1(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.Sauce_Labs_Backpack_Image_click()

        time.sleep(2)

        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/inventory-item.html?id=4"

        if current_url == expected_url:
            log.info(f"✅ IMAGE: Correct Sauce Labs Backpack URL: {current_url}")
        else:
            log.error(f"❌ IMAGE: Incorrect Sauce Labs Backpack URL! Expected: {expected_url}, but got: {current_url}")

        assert current_url == expected_url, f"❌ IMAGE: Expected: {expected_url}, but got: {current_url}"