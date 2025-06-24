import pytest
from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.HomePage import HomePage
from Pages.ProductDetailPage import ProductDetailPage
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestCancelButtonBringsBackToCart(BaseTest):

    def test_cancel_button_brings_back_to_cart(self):

        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.Sauce_Labs_Backpack_Image_click()
        details_page = ProductDetailPage(self.driver, wait)
        details_page.add_backpack_to_cart_details_page()
        home_page.get_homepage_cart_icon_click()
        Cart_page = CartPage(self.driver, wait)
        Cart_page.cart_checkout_button_cart_page()

        checkout_page = CheckoutPage(self.driver, wait)
        checkout_page.cancel()

        Cart_page.verify_url("https://www.saucedemo.com/cart.html", "URL")

