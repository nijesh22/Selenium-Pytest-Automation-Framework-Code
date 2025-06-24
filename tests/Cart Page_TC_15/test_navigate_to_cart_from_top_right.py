import pytest
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestContinueShoppingButtonWorks(BaseTest):
    def test_continue_shopping_button_works(self):

        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.get_homepage_cart_icon_click()

        Cart_page = CartPage(self.driver, wait)
        Cart_page.verify_url("https://www.saucedemo.com/cart.html","URL")

