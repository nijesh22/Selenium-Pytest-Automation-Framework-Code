import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.FinishPage import FinishPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestPlaceOrderWithMultipleItemsFinish:
    def test_place_order_with_multiple_items_finish(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_and_bike_light()
        home_page.Sauce_Labs_Backpack_Image_click()

        home_page.get_homepage_cart_icon_click()
        Cart_page = CartPage(self.driver, wait)
        Cart_page.cart_checkout_button_cart_page()

        checkout_page = CheckoutPage(self.driver, wait)
        checkout_page.first_last_zip_validation("manu", "ragav", "12345")
        checkout_page.click_continue()

        finish_page = FinishPage(self.driver, wait)
        finish_page.click_finish()

        current_success_message = finish_page.thankyou_message()
        expected_success_message = "Thank you for your order!"

        assert current_success_message == expected_success_message, f"❌ Expected: '{expected_success_message}', but got: '{current_success_message}'"
        log.info(f"✅ Correct order successful message displayed: {current_success_message}")