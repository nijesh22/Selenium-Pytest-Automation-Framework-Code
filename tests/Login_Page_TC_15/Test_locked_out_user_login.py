import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.utils import Utils

@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestLockedOutUserLogin:
    def test_locked_out_user_login(self,login_page):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page.swag_labs_loginIsvalid("locked_out_user", "secret_sauce")
        login_page.swag_labs_login_button()

        errormessage = login_page.login_error_message()
        error_text = errormessage.text

        expected_error = "Epic sadface: Sorry, this user has been locked out."

        assert error_text == expected_error, f"❌ Expected error: '{expected_error}', but got: '{error_text}'"
        log.info("✅ Locked out user error message is correct.")