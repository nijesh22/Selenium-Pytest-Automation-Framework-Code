import pytest
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestContinueShoppingButtonWorks(BaseTest):
    def test_continue_shopping_button_works(self,home_page,cart_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.get_homepage_cart_icon_click()

        cart_items = cart_page.cart_is_empty_or_not_cart_page_element()

        Utils.assert_cart_is_empty(cart_items,0, log)