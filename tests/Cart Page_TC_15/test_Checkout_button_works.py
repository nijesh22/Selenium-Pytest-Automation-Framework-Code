import pytest
from tests.BaseTest import BaseTest


##@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestCheckoutButtonWorks(BaseTest):
    def test_checkout_button_works(self,home_page,cart_page,product_details_page):

        wait = self.login_to_saucedemo(self.driver)

        home_page.add_backpack_item_and_go_to_cart()

        cart_page.cart_checkout_button_cart_page()

        product_details_page.verify_url("https://www.saucedemo.com/checkout-step-one.html","URL")

