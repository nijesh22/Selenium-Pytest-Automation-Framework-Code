import pytest
from selenium.webdriver.support.ui import WebDriverWait

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
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
    def test_login_is_valid(self, username, password):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid(username, password)
        login_page.swag_labs_login_button()


        # current_url = self.driver.current_url
        # expected_url = "https://www.saucedemo.com/inventory.html"
        #
        # if current_url == expected_url:
        #     log.info(f"✅ Correct URL: {current_url}")
        # else:
        #     log.error(f"❌ Incorrect URL! Expected: {expected_url}, but got: {current_url}")
        #
        # assert current_url == expected_url, f"❌ Expected: {expected_url}, but got: {current_url}"

        home_page = HomePage(self.driver, wait)
        home_page.verify_url("https://www.saucedemo.com/inventory.html","URL")

