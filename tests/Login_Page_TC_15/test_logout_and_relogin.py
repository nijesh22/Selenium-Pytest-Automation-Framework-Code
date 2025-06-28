import pytest
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestLogoutAndReLogin(BaseTest):
    def test_logout_and_relogin(self,home_page):

        wait = self.login_to_saucedemo(self.driver)

        home_page.verify_url("https://www.saucedemo.com/inventory.html", "URL")

        home_page.open_menu_and_logout()

        self.login_to_saucedemo(self.driver)
        home_page.verify_url("https://www.saucedemo.com/inventory.html", "URL")

