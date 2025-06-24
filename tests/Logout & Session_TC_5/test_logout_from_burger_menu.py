import pytest
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestLogoutFromBurgerMenu(BaseTest):
    def test_logout_from_burger_menu(self):

        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.open_menu_and_logout()


        login_page = LoginPage(self.driver, wait)
        login_page.verify_url("https://www.saucedemo.com/", "URL")

