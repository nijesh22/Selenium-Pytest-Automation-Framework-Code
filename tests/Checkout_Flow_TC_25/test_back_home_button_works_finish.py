import pytest
from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.FinishPage import FinishPage
from Pages.HomePage import HomePage
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestBackHomeButtonWorksFinish(BaseTest):
    def test_back_home_button_works_finish(self):

        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_to_cart()
        home_page.Sauce_Labs_Backpack_Image_click()

        home_page.get_homepage_cart_icon_click()
        Cart_page = CartPage(self.driver, wait)
        Cart_page.cart_checkout_button_cart_page()

        checkout_page = CheckoutPage(self.driver, wait)
        checkout_page.fill_checkout_info_and_click_continue("manu", "ragav", "12345")

        finish_page = FinishPage(self.driver, wait)
        finish_page.click_finish()

        finish_page.click_back_home_button()

        home_page.verify_url("https://www.saucedemo.com/inventory.html","URL")