import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils

@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestLockedOutUserLogin:
    def test_locked_out_user_login(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("locked_out_user", "secret_sauce")
        login_page.swag_labs_login_button()

        # Wait for error message to appear
        errormessage = login_page.login_error_message()
        error_text = errormessage.text

        # Expected error message
        expected_error = "Epic sadface: Sorry, this user has been locked out."

        # Assertion
        assert error_text == expected_error, f"❌ Expected error: '{expected_error}', but got: '{error_text}'"
        log.info("✅ Locked out user error message is correct.")