import pytest
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestOpenCloseBurgerMenu(BaseTest):
    def test_open_close_burger_menu(self):

        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.click_menu()
        home_page.side_menu_close_button()

        home_page.click_menu()
        home_page.side_menu_close_button()