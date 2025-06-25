import pytest
from Pages.HomePage import HomePage
from Pages.ProductDetailPage import ProductDetailPage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestProductDescriptionMatching(BaseTest):
    def test_product_description_matching(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        product_detail_page = ProductDetailPage(self.driver, wait)

        product_count = len(home_page.get_product_desc_elements())

        for i in range(product_count):
            product_desc = home_page.get_product_desc_by_index(i)
            home_page.click_product_by_index(i)

            product_desc_details_page = product_detail_page.get_product_desc_text()

            Utils.assert_text_match(product_desc, product_desc_details_page, "Product Description", log)

            self.driver.back()