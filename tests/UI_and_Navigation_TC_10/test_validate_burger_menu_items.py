import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestValidateBurgerMenuItems(BaseTest):
    def test_validate_burger_menu_items(self):

        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.click_menu()
        home_page.side_menu_about_button()

        login_page = LoginPage(self.driver, wait)
        login_page.verify_url("https://saucelabs.com/", "Sauce Labs URL")

        self.driver.back()

        home_page.click_menu()
        home_page.side_menu_Alliteams_button()

        home_page.verify_url("https://www.saucedemo.com/inventory.html","URL")

        home_page.click_logout()

        login_page.verify_url("https://www.saucedemo.com/", "URL")




