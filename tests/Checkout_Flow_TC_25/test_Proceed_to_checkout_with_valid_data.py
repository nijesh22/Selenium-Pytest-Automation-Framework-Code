import pytest
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestProceedToCheckoutWithValidData(BaseTest):
    def test_proceed_to_checkout_with_valid_data(self,home_page,cart_page,checkout_page):

        wait = self.login_to_saucedemo(self.driver)

        home_page.add_backpack_item_and_go_to_cart()

        cart_page.cart_checkout_button_cart_page()

        checkout_page.verify_url("https://www.saucedemo.com/checkout-step-one.html" , "URL")