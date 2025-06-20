import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestValidateBurgerMenuItems:
    def test_validate_burger_menu_items(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.click_menu()
        home_page.side_menu_about_button()

        current_url = self.driver.current_url
        expected_url = "https://saucelabs.com/"

        if current_url == expected_url:
            log.info(f"✅ Correct Sauce Labs URL: {current_url}")
        else:
            log.error(f"❌ Incorrect Sauce Labs URL! Expected: {expected_url}, but got: {current_url}")

        assert current_url == expected_url, f"❌ URL Expected: {expected_url}, but got: {current_url}"

        self.driver.back()

        home_page.click_menu()
        home_page.side_menu_Alliteams_button()

        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"

        if current_url == expected_url:
            log.info(f"✅ Correct inventory URL: {current_url}")
        else:
            log.error(f"❌ Incorrect inventory URL! Expected: {expected_url}, but got: {current_url}")

        assert current_url == expected_url, f"❌ URL Expected: {expected_url}, but got: {current_url}"

        home_page.click_logout()

        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/"

        if current_url == expected_url:
            log.info(f"✅ Correct login URL: {current_url}")
        else:
            log.error(f"❌ Correct login URL! Expected: {expected_url}, but got: {current_url}")

        assert current_url == expected_url, f"❌ URL Expected: {expected_url}, but got: {current_url}"


