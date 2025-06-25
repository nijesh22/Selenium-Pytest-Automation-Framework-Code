import pytest
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestSortByPriceHighToLow(BaseTest):
    def test_sort_price_high_to_low(self,home_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.select_sort_option("Price (high to low)")
        ui_prices = home_page.get_product_prices()

        expected_sorted_prices = sorted(ui_prices , reverse= True)

        Utils.assert_list_sorted(ui_prices, expected_sorted_prices, "Product price high to low", log)



