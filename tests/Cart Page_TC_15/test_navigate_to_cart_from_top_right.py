import pytest
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestContinueShoppingButtonWorks(BaseTest):
    def test_continue_shopping_button_works(self,home_page,cart_page):

        wait = self.login_to_saucedemo(self.driver)

        home_page.get_homepage_cart_icon_click()

        cart_page.verify_url("https://www.saucedemo.com/cart.html","URL")

