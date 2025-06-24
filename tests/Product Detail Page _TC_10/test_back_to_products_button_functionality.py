import pytest
from Pages.HomePage import HomePage
from Pages.ProductDetailPage import ProductDetailPage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestAddProductToCartFromDetailPage(BaseTest):
    def test_add_product_to_cart_from_detail_page(self):

        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.Sauce_Labs_Backpack_Image_click()

        home_page.verify_url("https://www.saucedemo.com/inventory-item.html?id=4" , "URL")

        details_page = ProductDetailPage(self.driver, wait)
        details_page.back_to_products_details_page()

        home_page.verify_url("https://www.saucedemo.com/inventory.html" , "URL")