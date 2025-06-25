import pytest
from Pages.CartPage import CartPage
from Pages.CheckOutOverview import CheckOutOverview
from Pages.CheckOutPage import CheckoutPage
from Pages.HomePage import HomePage
from Pages.ProductDetailPage import ProductDetailPage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestVerifyProductListMatchesCartOverview(BaseTest):
    def test_verify_product_list_matches_cart_overview(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_to_cart()
        home_page.Sauce_Labs_Backpack_Image_click()
        product_detail_page = ProductDetailPage(self.driver, wait)

        product_details_name = product_detail_page.get_product_details_name()
        product_details_desc = product_detail_page.get_product_details_desc()
        product_details_price = product_detail_page.get_product_details_price()

        home_page.get_homepage_cart_icon_click()
        Cart_page = CartPage(self.driver, wait)
        Cart_page.cart_checkout_button_cart_page()

        checkout_page = CheckoutPage(self.driver, wait)
        checkout_page.fill_checkout_info_and_click_continue("manu", "ragav", "12345")

        checkout_overview_page = CheckOutOverview(self.driver, wait)
        name = checkout_overview_page.get_overview_product_name()
        desc = checkout_overview_page.get_overview_product_desc()
        price = checkout_overview_page.get_overview_product_price()

        Utils.assert_text_match(product_details_name, name, "Product Name", log)

        Utils.assert_text_match(product_details_desc, desc, "Product Description", log)

        Utils.assert_text_match(product_details_price, price, "Product price", log)

