import pytest
from Pages.HomePage import HomePage
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestLogoutAndReLogin(BaseTest):
    def test_logout_and_relogin(self):

        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.verify_url("https://www.saucedemo.com/inventory.html", "URL")

        #Logout
        home_page.open_menu_and_logout()

        #Relogin
        self.login_to_saucedemo(self.driver)
        home_page.verify_url("https://www.saucedemo.com/inventory.html", "URL")

