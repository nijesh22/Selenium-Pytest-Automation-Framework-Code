import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestOpenCloseBurgerMenu(BaseTest):
    def test_open_close_burger_menu(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        # wait = WebDriverWait(self.driver, 10)
        # login_page = LoginPage(self.driver, wait)
        # login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        # login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.click_menu()
        home_page.side_menu_close_button()

        home_page.click_menu()
        home_page.side_menu_close_button()