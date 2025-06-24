import pytest
from Pages.CartPage import CartPage
from Pages.CheckOutOverview import CheckOutOverview
from Pages.CheckOutPage import CheckoutPage
from Pages.HomePage import HomePage
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestCancelBringsBackToCartOverview(BaseTest):
    def test_cancel_brings_back_to_cart_overview(self):

        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_to_cart()
        home_page.Sauce_Labs_Backpack_Image_click()

        home_page.get_homepage_cart_icon_click()
        Cart_page = CartPage(self.driver, wait)
        Cart_page.cart_checkout_button_cart_page()

        checkout_page = CheckoutPage(self.driver, wait)
        checkout_page.fill_checkout_info_and_click_continue("manu", "ragav", "12345")

        checkout_overview_page = CheckOutOverview(self.driver, wait)
        checkout_overview_page.click_cancel()

        home_page.verify_url("https://www.saucedemo.com/inventory.html" , "URL")
