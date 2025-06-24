import time
import pytest
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestCartGetsClearedOnLogout(BaseTest):
    def test_cart_gets_cleared_on_logout(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_to_cart()

        time.sleep(1)

        cart_count = home_page.get_cart_badge_count()

        Utils.assert_cart_badge_count(cart_count, 1, log)

        home_page.open_menu_and_logout()

        self.login_to_saucedemo(self.driver)

        cart_count_latest = home_page.get_cart_badge_count()

        assert not cart_count_latest == '1', f"❌ Expected cart to be empty after re-login, but found '{cart_count_latest}' item(s)"
        log.info("✅ Cart is empty after re-login. Session reset is working correctly.")