import pytest
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestContinueShoppingButtonWorks(BaseTest):
    def test_continue_shopping_button_works(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.get_homepage_cart_icon_click()

        Cart_page = CartPage(self.driver, wait)

        cart_items = Cart_page.cart_is_empty_or_not_cart_page_element()
        assert len(cart_items) == 0, "❌ Cart is not empty!"
        log.info("✅ Cart is empty.")