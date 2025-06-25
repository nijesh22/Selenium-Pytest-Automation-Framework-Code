import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestInvalidLoginCases(BaseTest):

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

    def test_invalid_login_cases(self,login_page, username, password):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)

        login_page.swag_labs_loginIsvalid(username, password)
        login_page.swag_labs_login_button()

        errormessage = login_page.login_error_message()
        error_text = errormessage.text

        expected_error = "Epic sadface: Username and password do not match any user in this service"

        assert error_text == expected_error, f"❌ Expected error: '{expected_error}', but got: '{error_text}'"
        log.info("✅ invalid username & invalid password correct error message is displayed")


