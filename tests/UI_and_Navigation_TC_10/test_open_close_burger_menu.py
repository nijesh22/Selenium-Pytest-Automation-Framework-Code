import pytest
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestOpenCloseBurgerMenu(BaseTest):
    def test_open_close_burger_menu(self,home_page):

        wait = self.login_to_saucedemo(self.driver)

        home_page.open_and_close_side_menu()

        home_page.open_and_close_side_menu()