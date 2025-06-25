import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestVerifyProductListMatchesCartOverview(BaseTest):
    def test_verify_product_list_matches_cart_overview(self,home_page,product_details_page,cart_page,checkout_page,checkout_overview_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.add_backpack_to_cart()
        home_page.Sauce_Labs_Backpack_Image_click()

        product_details_name = product_details_page.get_product_details_name()
        product_details_desc = product_details_page.get_product_details_desc()
        product_details_price = product_details_page.get_product_details_price()

        home_page.get_homepage_cart_icon_click()
        cart_page.cart_checkout_button_cart_page()

        checkout_page.fill_checkout_info_and_click_continue("manu", "ragav", "12345")

        name = checkout_overview_page.get_overview_product_name()
        desc = checkout_overview_page.get_overview_product_desc()
        price = checkout_overview_page.get_overview_product_price()

        Utils.assert_text_match(product_details_name, name, "Product Name", log)

        Utils.assert_text_match(product_details_desc, desc, "Product Description", log)

        Utils.assert_text_match(product_details_price, price, "Product price", log)

