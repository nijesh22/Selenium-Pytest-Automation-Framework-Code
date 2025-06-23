import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestSessionResetAfterLogout:
    def test_session_reset_after_logout(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.click_menu()
        home_page.click_logout()

        # current_url = self.driver.current_url
        # expected_url = "https://www.saucedemo.com/"
        #
        # if current_url == expected_url:
        #     log.info(f"✅ Correct URL: {current_url}")
        # else:
        #     log.error(f"❌ Incorrect URL! Expected: {expected_url}, but got: {current_url}")
        #
        # assert current_url == expected_url, f"❌ Expected: {expected_url}, but got: {current_url}"

        login_page.verify_url("https://www.saucedemo.com/" , "URL")

        self.driver.get("https://www.saucedemo.com/inventory.html")

        assert login_page.get_session_error_message() == "Epic sadface: You can only access '/inventory.html' when you are logged in.", \
            "❌ Session did not reset — was able to access inventory without being logged in"
        log.info("✅ Session reset working as expected. Protected page can't be accessed after logout.")