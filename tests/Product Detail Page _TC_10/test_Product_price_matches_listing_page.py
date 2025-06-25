import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestProductPriceMatchesListing(BaseTest):
    def test_product_price_matches_listing(self,home_page,product_details_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        product_count = len(home_page.get_product_price_elements())

        for i in range(product_count):
            product_price = home_page.get_product_price_by_index(i)
            home_page.click_product_by_index(i)

            product_price_details_page = product_details_page.get_product_price()

            Utils.assert_text_match(product_price, product_price_details_page, "Product Price", log)

            self.driver.back()