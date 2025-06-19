import pytest
from selenium.webdriver.support.ui import WebDriverWait
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestAddRemoveAfterSorting:
    def test_AddRemove_after_sorting(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)

        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

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
            assert badge_count == '1', f"❌ Cart badge should show 1 after adding. Got: '{badge_count}'"
            log.info("🛒 ✅ Cart badge shows 1 after adding product.")

            # Remove product from cart
            home_page.remove_backpack_from_cart()

            # ✅ Assert cart badge is gone
            badge_count_after_removal = home_page.get_cart_badge_count()
            assert badge_count_after_removal == '' or badge_count_after_removal == '0', \
                f"❌ Cart should be empty after removal. Got: '{badge_count_after_removal}'"
            log.info("🗑️ ✅ Cart is empty after removing product.")