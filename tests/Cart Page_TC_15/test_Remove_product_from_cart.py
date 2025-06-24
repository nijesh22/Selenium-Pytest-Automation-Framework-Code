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

        assert cart_count_after_removal == '0', f"❌ Expected cart badge to show '0', but got '{cart_count_after_removal}'"
        log.info("✅ Cart badge correctly shows 0 item in details page.")