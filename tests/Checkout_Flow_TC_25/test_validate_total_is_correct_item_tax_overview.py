import math
import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestValidateTotalIsCorrectItemTax(BaseTest):
    def test_validate_total_is_correct_item_tax(self,home_page,cart_page,checkout_page,checkout_overview_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.add_backpack_to_cart()
        home_page.Sauce_Labs_Backpack_Image_click()

        home_page.get_homepage_cart_icon_click()

        cart_page.cart_checkout_button_cart_page()

        checkout_page.fill_checkout_info_and_click_continue("manu", "ragav", "12345")

        item_total = checkout_overview_page.get_item_total()
        tax = checkout_overview_page.get_tax()
        total_ui = checkout_overview_page.get_total()

        expected_total = item_total + tax

        assert math.isclose(expected_total, total_ui, rel_tol=1e-2), (
            f"❌ Total mismatch! Expected: {expected_total}, Found: {total_ui}"
        )

        log.info("✅ Total is correct (Item Total + Tax).")