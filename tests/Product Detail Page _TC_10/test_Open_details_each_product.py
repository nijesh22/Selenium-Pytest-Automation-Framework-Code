import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestOpenDetailsEachProduct(BaseTest):
    def test_open_details_each_product(self,home_page,product_details_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        product_count = len(home_page.get_product_elements())
        for i in range(product_count):
            product_name = home_page.get_product_name_by_index(i)
            home_page.click_product_by_index(i)

            detail_title = product_details_page.get_product_title()

            Utils.assert_text_match(product_name, detail_title, "Product Name", log)

            self.driver.back()