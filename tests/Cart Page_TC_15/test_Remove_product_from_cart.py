import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestRemoveProductFromCart(BaseTest):
    def test_remove_product_from_cart(self,home_page,cart_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.add_backpack_item_and_go_to_cart()

        cart_page.cart_remove_product_cart_page()

        cart_count_after_removal = home_page.get_cart_badge_count()

        Utils.assert_cart_badge_count(cart_count_after_removal, 0, log)