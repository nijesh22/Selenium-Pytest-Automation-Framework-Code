import pytest
from selenium.webdriver.support.ui import WebDriverWait
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestSortByPriceLowToHigh(BaseTest):
    def test_sort_price_low_to_high(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        # log = Utils.customlogger()
        # wait = WebDriverWait(self.driver, 10)
        # login_page = LoginPage(self.driver, wait)
        # login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        # login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.select_sort_option("Price (low to high)")
        ui_prices = home_page.get_product_prices()

        expected_sorted_prices = sorted(ui_prices)

        assert ui_prices == expected_sorted_prices, f"❌ Prices not sorted Low to High. Got: {ui_prices}"
        log.info("✅ Product prices are sorted Low to High correctly.")
