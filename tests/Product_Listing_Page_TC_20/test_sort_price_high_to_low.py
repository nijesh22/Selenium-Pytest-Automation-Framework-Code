import pytest
from selenium.webdriver.support.ui import WebDriverWait
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestSortByPriceHighToLow:
    def test_sort_price_high_to_low(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)

        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.select_sort_option("Price (high to low)")
        ui_prices = home_page.get_product_prices()

        expected_sorted_prices = sorted(ui_prices , reverse= True)

        assert ui_prices == expected_sorted_prices, f"❌ Prices not sorted high to low. Got: {ui_prices}"
        log.info("✅ Product prices are sorted high to low correctly.")
