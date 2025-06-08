import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from Pages.LoginPage import LoginPage


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class Test_validlogin:

    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            ("problem_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce"),
            ("error_user", "secret_sauce"),
            ("visual_user", "secret_sauce"),
        ],
        ids=[
            "standard_user",
            "problem_user",
            "performance_glitch_user",
            "error_user",
            "visual_user"
        ]
    )
    def test_loginisvalid(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid(username, password)
        login_page.swag_labs_login_button()
        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"

        if current_url == expected_url:
            print(f"✅ Correct URL: {current_url}")
        else:
            print(f"❌ Incorrect URL! Expected: {expected_url}, but got: {current_url}")

        assert current_url == expected_url, f"❌ Expected: {expected_url}, but got: {current_url}"


