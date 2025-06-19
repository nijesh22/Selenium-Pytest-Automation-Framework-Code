import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class Test_Proceed_with_blank_fields_expect_error:
    def test_Proceed_with_blank_fields_expect_error_1(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.get_homepage_cart_icon_click()

        Cart_page = CartPage(self.driver, wait)

        cart_items = Cart_page.cart_is_empty_or_not_cart_page_element()
        assert len(cart_items) == 0, "❌ Cart is not empty!"
        log.info("✅ Cart is empty.")

        Cart_page.cart_checkout_button_cart_page()

        time.sleep(3)

        checkout = CheckoutPage(self.driver, wait)
        assert not checkout.is_on_step_one(), "❌ Bug: Checkout allowed with empty cart to step one!"