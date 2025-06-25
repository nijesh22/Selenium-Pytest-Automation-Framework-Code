import time
import pytest
from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestProceedWithBlankFieldsExpectError(BaseTest):
    def test_proceed_with_blank_fields_expect_error(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.get_homepage_cart_icon_click()

        Cart_page = CartPage(self.driver, wait)

        cart_items = Cart_page.cart_is_empty_or_not_cart_page_element()

        Utils.assert_cart_is_empty(cart_items, 0,log)

        Cart_page.cart_checkout_button_cart_page()

        time.sleep(3)

        checkout = CheckoutPage(self.driver, wait)
        assert not checkout.is_on_step_one(), "❌ Bug: Checkout allowed with empty cart to step one!"