import pytest
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestCancelBringsBackToCartOverview(BaseTest):
    def test_cancel_brings_back_to_cart_overview(self,home_page,cart_page,checkout_page,checkout_overview_page):

        wait = self.login_to_saucedemo(self.driver)

        home_page.add_backpack_to_cart()
        home_page.Sauce_Labs_Backpack_Image_click()

        home_page.get_homepage_cart_icon_click()
        cart_page.cart_checkout_button_cart_page()

        checkout_page.fill_checkout_info_and_click_continue("manu", "ragav", "12345")

        checkout_overview_page.click_cancel()

        home_page.verify_url("https://www.saucedemo.com/inventory.html" , "URL")
