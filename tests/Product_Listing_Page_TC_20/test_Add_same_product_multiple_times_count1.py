import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class Test_remove_product_from_cart:
    def test_remove_product_from_cart_1(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_to_cart()

        time.sleep(1)

        cart_count = home_page.get_cart_badge_count()

        assert cart_count == '1', f"❌ Expected cart badge to show '1', but got '{cart_count}'"
        log.info("✅ Cart badge correctly shows 1 item.")

        home_page.remove_backpack_from_cart()

        time.sleep(1)

        cart_count_after_removal = home_page.get_cart_badge_count()
        assert cart_count_after_removal == '0', f"❌ Expected cart badge to show '0', but got '{cart_count_after_removal}'"
        log.info("✅ Cart badge correctly shows 0 item.")

        home_page.add_backpack_to_cart()

        time.sleep(3)

        cart_count = home_page.get_cart_badge_count()

        assert cart_count == '1', f"❌ Expected cart badge to show '1', but got '{cart_count}'"
        log.info("✅ Cart badge correctly shows 1 item.")

        home_page.remove_backpack_from_cart()

        time.sleep(3)

        cart_count_after_removal = home_page.get_cart_badge_count()
        assert cart_count_after_removal == '0', f"❌ Expected cart badge to show '0', but got '{cart_count_after_removal}'"
        log.info("✅ Cart badge correctly shows 0 item.")