import math
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
class TestValidateTotalIsCorrectItemTax(BaseTest):
    def test_validate_total_is_correct_item_tax(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        # log = Utils.customlogger()
        # wait = WebDriverWait(self.driver, 10)
        # login_page = LoginPage(self.driver, wait)
        # login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        # login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_to_cart()
        home_page.Sauce_Labs_Backpack_Image_click()

        home_page.get_homepage_cart_icon_click()
        Cart_page = CartPage(self.driver, wait)
        Cart_page.cart_checkout_button_cart_page()

        checkout_page = CheckoutPage(self.driver, wait)
        checkout_page.first_last_zip_validation("manu", "ragav", "12345")
        checkout_page.click_continue()

        CheckOutOverviews = CheckOutOverview(self.driver, wait)

        item_total = CheckOutOverviews.get_item_total()
        tax = CheckOutOverviews.get_tax()
        total_ui = CheckOutOverviews.get_total()

        expected_total = item_total + tax

        assert math.isclose(expected_total, total_ui, rel_tol=1e-2), (
            f"❌ Total mismatch! Expected: {expected_total}, Found: {total_ui}"
        )

        log.info("✅ Total is correct (Item Total + Tax).")