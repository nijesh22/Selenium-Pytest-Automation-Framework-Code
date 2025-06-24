import pytest
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestAddRemoveAfterSorting(BaseTest):
    def test_add_remove_after_sorting(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)

        sort_options = [
            "Name (A to Z)",
            "Name (Z to A)",
            "Price (high to low)",
            "Price (low to high)"
        ]

        for option in sort_options:
            log.info(f"\n🔄 Testing sort: {option}")

            # Apply sort option
            home_page.select_sort_option(option)

            # Add product to cart
            home_page.add_backpack_to_cart()

            # ✅ Assert cart badge shows 1
            badge_count = home_page.get_cart_badge_count()

            Utils.assert_cart_badge_count(badge_count, 1, log)

            # Remove product from cart
            home_page.remove_backpack_from_cart()

            # ✅ Assert cart badge is gone
            badge_count_after_removal = home_page.get_cart_badge_count()
            assert badge_count_after_removal == '' or badge_count_after_removal == '0', \
                f"❌ Cart should be empty after removal. Got: '{badge_count_after_removal}'"
            log.info("🗑️ ✅ Cart is empty after removing product.")