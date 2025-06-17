import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage

#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class Test_cart_gets_cleared_on_logout:
    def test_cart_gets_cleared_on_logout_1(self):
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_to_cart()

        time.sleep(3)

        cart_count = home_page.get_cart_badge_count()

        assert cart_count == '1', f"❌ Expected cart badge to show '1', but got '{cart_count}'"
        print("✅ Cart badge correctly shows 1 item.")

        home_page.click_menu()
        home_page.click_logout()

        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        cart_count_latest = home_page.get_cart_badge_count()

        assert not cart_count_latest == '1', f"❌ Expected cart to be empty after re-login, but found '{cart_count_latest}' item(s)"
        print("✅ Cart is empty after re-login. Session reset is working correctly.")