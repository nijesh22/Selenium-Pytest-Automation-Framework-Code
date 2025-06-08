import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.LoginPage import LoginPage

#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestLoginWithBlankInputs:

    @pytest.mark.parametrize(
        "username, password, expected_error",
        [
            ("", "", "Epic sadface: Username is required"),
            ("", "secret_sauce", "Epic sadface: Username is required"),
            ("standard_user", "", "Epic sadface: Password is required"),
            ("   ", "   ", "Epic sadface: Username and password do not match any user in this service"),  # Whitespaces treated as blank
            ("standard_user@", "test@123", "Epic sadface: Username and password do not match any user in this service")
        ],
        ids=[
            "Blank username and password",
            "Blank username only",
            "Blank password only",
            "Login with whitespace inputs",
            "Login with special characters"
        ]
    )
    def test_login_with_blank_inputs_1(self, username, password, expected_error):
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)

        login_page.swag_labs_loginIsvalid(username, password)
        login_page.swag_labs_login_button()

        errormessage = login_page.login_error_message()
        error_text = errormessage.text

        # Assertion
        assert error_text == expected_error, f"❌ Expected: '{expected_error}', but got: '{error_text}'"
        print(f"✅ Correct error message displayed: {error_text}")

