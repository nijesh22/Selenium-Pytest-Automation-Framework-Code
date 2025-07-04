import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestClickFinishAndValidateSuccessFinish(BaseTest):
    def test_click_finish_and_validate_success_finish(self,home_page,cart_page,checkout_page,finish_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.add_backpack_to_cart()
        home_page.Sauce_Labs_Backpack_Image_click()

        home_page.get_homepage_cart_icon_click()

        cart_page.cart_checkout_button_cart_page()


        checkout_page.fill_checkout_info_and_click_continue("manu", "ragav", "12345")

        finish_page.click_finish()

        current_success_message = finish_page.thankyou_message()
        expected_success_message = "Thank you for your order!"

        Utils.assert_text_equals(current_success_message, expected_success_message, "Order Success Message", log)
