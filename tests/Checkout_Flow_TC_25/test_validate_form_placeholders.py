import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProductDetailPage import ProductDetailPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class Test_validate_form_placeholders:

    def test_validate_form_placeholders_1(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.Sauce_Labs_Backpack_Image_click()
        details_page = ProductDetailPage(self.driver, wait)
        details_page.add_backpack_to_cart_details_page()
        home_page.get_homepage_cart_icon_click()
        Cart_page = CartPage(self.driver, wait)
        Cart_page.cart_checkout_button_cart_page()

        checkout_page = CheckoutPage(self.driver, wait)

        assert checkout_page.get_first_name_placeholder() == "First Name", "❌ First Name placeholder is incorrect"
        assert checkout_page.get_last_name_placeholder() == "Last Name", "❌ Last Name placeholder is incorrect"
        assert checkout_page.get_postal_code_placeholder() == "Zip/Postal Code", "❌ Postal Code placeholder is incorrect"

        log.info("✅ All placeholder texts are correctly displayed")