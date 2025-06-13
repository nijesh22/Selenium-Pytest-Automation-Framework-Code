import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class Test_continue_shopping_button_works:
    def test_continue_shopping_button_works_1(self):
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.get_homepage_cart_icon_click()

        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/cart.html"

        if current_url == expected_url:
            print(f"✅ Correct URL: {current_url}")
        else:
            print(f"❌ Incorrect URL! Expected: {expected_url}, but got: {current_url}")

        assert current_url == expected_url, f"❌ Expected: {expected_url}, but got: {current_url}"

