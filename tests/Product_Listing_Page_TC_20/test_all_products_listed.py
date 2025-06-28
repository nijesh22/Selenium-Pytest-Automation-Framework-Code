import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestAllProductsListed(BaseTest):
    def test_all_products_listed(self,home_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        product_list = home_page.get_all_products()

        log.info(" Products found on page:")
        for product in product_list:
            print(" -", product.text)

        assert len(product_list) == 6, f"❌ Expected 6 products, but found {len(product_list)}"
        log.info("✅ All 6 products are found.")
