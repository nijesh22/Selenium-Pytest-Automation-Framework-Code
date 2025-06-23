import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestProceedToCheckoutWithValidData(BaseTest):
    def test_proceed_to_checkout_with_valid_data(self):

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

        Cart_page = CartPage(self.driver, wait)

        Cart_page.cart_checkout_button_cart_page()

        # current_url = self.driver.current_url
        # expected_url = "https://www.saucedemo.com/checkout-step-one.html"
        #
        # if current_url == expected_url:
        #     log.info(f"✅ Correct URL: {current_url}")
        # else:
        #     log.error(f"❌ Incorrect URL! Expected: {expected_url}, but got: {current_url}")
        #
        # assert current_url == expected_url, f"❌ Expected: {expected_url}, but got: {current_url}"
        checkout_page = CheckoutPage(self.driver, wait)
        checkout_page.verify_url("https://www.saucedemo.com/checkout-step-one.html" , "URL")