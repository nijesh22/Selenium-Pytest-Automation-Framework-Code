import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestSortByPriceLowToHigh(BaseTest):
    def test_sort_price_low_to_high(self,home_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.select_sort_option("Price (low to high)")
        ui_prices = home_page.get_product_prices()

        expected_sorted_prices = sorted(ui_prices)

        Utils.assert_list_sorted(ui_prices, expected_sorted_prices, "Product price Low to High", log)
