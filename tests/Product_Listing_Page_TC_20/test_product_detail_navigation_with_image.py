import time
import pytest
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestProductDetailNavigationWithImage(BaseTest):
    def test_product_detail_navigation(self,home_page,product_details_page):

        wait = self.login_to_saucedemo(self.driver)

        home_page.Sauce_Labs_Backpack_Image_click()

        time.sleep(2)

        product_details_page.verify_url("https://www.saucedemo.com/inventory-item.html?id=4", "URL")