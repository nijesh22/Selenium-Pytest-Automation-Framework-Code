import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest

#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestValidateAddedProductsInCart(BaseTest):
    def test_validate_added_products_in_cart(self,home_page,product_details_page,cart_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.add_backpack_to_cart()
        home_page.Sauce_Labs_Backpack_Image_click()

        product_details_name = product_details_page.get_product_details_name()
        product_details_desc = product_details_page.get_product_details_desc()
        product_details_price = product_details_page.get_product_details_price()

        home_page.get_homepage_cart_icon_click()

        cart_page_name = cart_page.get_cart_product_name()
        cart_page_desc = cart_page.get_cart_product_desc()
        cart_page_price = cart_page.get_cart_product_price()

        Utils.assert_text_match(product_details_name, cart_page_name, "Product Name", log)

        Utils.assert_text_match(product_details_desc, cart_page_desc, "Product description", log)

        Utils.assert_text_match(product_details_price, cart_page_price, "Product price", log)
