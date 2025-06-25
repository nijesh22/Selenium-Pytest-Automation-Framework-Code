import pytest
from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.FinishPage import FinishPage
from Pages.HomePage import HomePage
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestPlaceOrderWithMultipleItemsFinish(BaseTest):
    def test_place_order_with_multiple_items_finish(self,home_page,cart_page,checkout_page,finish_page):

        wait = self.login_to_saucedemo(self.driver)

        home_page.Sauce_Labs_Backpack_Image_click()

        home_page.get_homepage_cart_icon_click()

        cart_page.cart_checkout_button_cart_page()

        checkout_page.fill_checkout_info_and_click_continue("manu", "ragav", "12345")

        finish_page.click_finish()

        assert not finish_page.is_on_checkout_complete(), "❌ Bug Found : Order completed without adding any products in cart!"