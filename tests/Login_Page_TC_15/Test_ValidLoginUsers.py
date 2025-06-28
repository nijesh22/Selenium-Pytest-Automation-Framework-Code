import pytest
from selenium.webdriver.support.ui import WebDriverWait

#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestValidLogin:

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
    def test_login_is_valid(self,login_page,home_page, username, password):

        wait = WebDriverWait(self.driver, 10)

        login_page.swag_labs_loginIsvalid(username, password)
        login_page.swag_labs_login_button()

        home_page.verify_url("https://www.saucedemo.com/inventory.html","URL")

