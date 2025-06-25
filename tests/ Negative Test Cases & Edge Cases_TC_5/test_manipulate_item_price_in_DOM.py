import time

import pytest
from Pages.CartPage import CartPage
from Pages.CheckOutOverview import CheckOutOverview
from Pages.CheckOutPage import CheckoutPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestManipulateItemPriceInDOM(BaseTest):
    def test_manipulate_item_price_in_dom(self,home_page,cart_page,checkout_page,checkout_overview_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.add_backpack_item_and_go_to_cart()

        cart_page.change_cart_price_from_DOM()

        cart_page.cart_checkout_button_cart_page()

        checkout_page.fill_checkout_info_and_click_continue("manu", "ragav", "12345")

        price = checkout_overview_page.get_overview_product_price()

        expected_price = '$29.99'

        assert price == expected_price, f"❌ Price Mismatch After DOM Manipulation! Expected: {price}"
        log.info(f"✅ {price} Price correctly displayed.")

