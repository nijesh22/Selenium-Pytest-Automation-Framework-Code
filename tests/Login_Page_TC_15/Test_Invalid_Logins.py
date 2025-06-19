import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.LoginPage import LoginPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class Test_Invalid_Login_Cases:

    @pytest.mark.parametrize("username, password", [
        ("invlaidusernametest", "secret_sauce"),
        ("standard_user", "p@ssword@123"),
        ("testuser", "test@123")
    ],
    ids=[
        "Invalid Username + Valid Password",
        "Valid Username + Invalid Password",
        "Both Username and Password Invalid"
        ]
    )

    def test_Invalid_Login_Cases_1(self, username, password):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid(username, password)
        login_page.swag_labs_login_button()

        # Wait for error message to appear
        errormessage = login_page.login_error_message()
        error_text = errormessage.text

        # Expected error message
        expected_error = "Epic sadface: Username and password do not match any user in this service"

        # Assertion
        assert error_text == expected_error, f"❌ Expected error: '{expected_error}', but got: '{error_text}'"
        log.info("✅ invalid username & invalid password correct error message is displayed")


