import time
import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestRemoveProductFromCart(BaseTest):
    def test_remove_product_from_cart(self,home_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.add_backpack_to_cart()

        time.sleep(1)

        cart_count = home_page.get_cart_badge_count()

        Utils.assert_cart_badge_count(cart_count, 1, log)

        home_page.remove_backpack_from_cart()

        time.sleep(1)

        cart_count_after_removal = home_page.get_cart_badge_count()

        Utils.assert_cart_badge_count(cart_count_after_removal, 0, log)

        home_page.add_backpack_to_cart()

        time.sleep(3)

        cart_count = home_page.get_cart_badge_count()

        Utils.assert_cart_badge_count(cart_count, 1, log)

        home_page.remove_backpack_from_cart()

        time.sleep(3)

        cart_count_after_removal = home_page.get_cart_badge_count()

        Utils.assert_cart_badge_count(cart_count_after_removal, 0, log)
