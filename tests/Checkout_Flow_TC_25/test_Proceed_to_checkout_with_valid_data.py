import pytest
from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.HomePage import HomePage
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestProceedToCheckoutWithValidData(BaseTest):
    def test_proceed_to_checkout_with_valid_data(self):

        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_item_and_go_to_cart()

        Cart_page = CartPage(self.driver, wait)

        Cart_page.cart_checkout_button_cart_page()

        checkout_page = CheckoutPage(self.driver, wait)
        checkout_page.verify_url("https://www.saucedemo.com/checkout-step-one.html" , "URL")