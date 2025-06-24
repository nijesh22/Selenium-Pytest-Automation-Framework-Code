import pytest
from Pages.HomePage import HomePage
from Pages.ProductDetailPage import ProductDetailPage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestOpenDetailsEachProduct(BaseTest):
    def test_open_details_each_product(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        product_detail_page = ProductDetailPage(self.driver, wait)

        product_count = len(home_page.get_product_elements())
        for i in range(product_count):
            product_name = home_page.get_product_name_by_index(i)
            home_page.click_product_by_index(i)

            detail_title = product_detail_page.get_product_title()

            assert product_name == detail_title, f"❌ Mismatch! Expected: {product_name}, Got: {detail_title}"
            log.info(f"✅ {product_name} page opened correctly.")

            self.driver.back()