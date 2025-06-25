import pytest
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestRemoveProductFromCart(BaseTest):
    def test_remove_product_from_cart(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_item_and_go_to_cart()

        cart_page = CartPage(self.driver, wait)
        cart_page.cart_remove_product_cart_page()
        cart_count_after_removal = home_page.get_cart_badge_count()

        Utils.assert_cart_badge_count(cart_count_after_removal, 0, log)

        Cart_page = CartPage(self.driver, wait)

        cart_items = Cart_page.cart_is_empty_or_not_cart_page_element()

        Utils.assert_cart_is_empty(cart_items,0, log)


