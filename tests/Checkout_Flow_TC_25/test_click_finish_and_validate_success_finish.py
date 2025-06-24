import pytest
from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.FinishPage import FinishPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestClickFinishAndValidateSuccessFinish(BaseTest):
    def test_click_finish_and_validate_success_finish(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_to_cart()
        home_page.Sauce_Labs_Backpack_Image_click()

        home_page.get_homepage_cart_icon_click()
        Cart_page = CartPage(self.driver, wait)
        Cart_page.cart_checkout_button_cart_page()

        checkout_page = CheckoutPage(self.driver, wait)
        checkout_page.fill_checkout_info_and_click_continue("manu", "ragav", "12345")

        finish_page = FinishPage(self.driver, wait)
        finish_page.click_finish()

        current_success_message = finish_page.thankyou_message()
        expected_success_message = "Thank you for your order!"

        assert current_success_message == expected_success_message, f"❌ Expected: '{expected_success_message}', but got: '{current_success_message}'"
        log.info(f"✅ Correct order successful message displayed: {current_success_message}")

