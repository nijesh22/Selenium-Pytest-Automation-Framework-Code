import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.CartPage import CartPage
from Pages.CheckOutOverview import CheckOutOverview
from Pages.CheckOutPage import CheckoutPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestManipulateItemPriceInDOM(BaseTest):
    def test_manipulate_item_price_in_dom(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)
        # log = Utils.customlogger()
        # wait = WebDriverWait(self.driver, 10)
        # login_page = LoginPage(self.driver, wait)
        # login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        # login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_to_cart()
        home_page.get_homepage_cart_icon_click()

        cart_page = CartPage(self.driver, wait)
        cart_page.change_cart_price_from_DOM()

        cart_page.cart_checkout_button_cart_page()

        checkout_page = CheckoutPage(self.driver, wait)
        checkout_page.first_last_zip_validation("manu", "ragav", "12345")
        checkout_page.click_continue()

        checkout_overview_page = CheckOutOverview(self.driver, wait)
        price = checkout_overview_page.get_overview_product_price()

        assert price == '$29.99', f"❌ Price Mismatch After DOM Manipulation! Expected: {price}"
        log.info(f"✅ {price} Price correctly displayed.")

