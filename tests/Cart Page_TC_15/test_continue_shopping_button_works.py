import pytest
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestContinueShoppingButtonWorks(BaseTest):

    def test_continue_shopping_button_works(self,home_page,cart_page):
        wait = self.login_to_saucedemo(self.driver)

        home_page.add_backpack_item_and_go_to_cart()

        cart_page.cart_continue_button_cart_page()

        home_page.verify_url("https://www.saucedemo.com/inventory.html","URL")