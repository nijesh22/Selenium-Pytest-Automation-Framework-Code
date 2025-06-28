import pytest
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestLogoutFromBurgerMenu(BaseTest):
    def test_logout_from_burger_menu(self,home_page,login_page):

        wait = self.login_to_saucedemo(self.driver)

        home_page.open_menu_and_logout()

        login_page.verify_url("https://www.saucedemo.com/", "URL")

