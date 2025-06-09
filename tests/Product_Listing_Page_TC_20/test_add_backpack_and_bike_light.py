import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage

@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class Test_add_backpack_and_bike_light:
    def test_add_backpack_and_bike_light_1(self):
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_and_bike_light()
        cart_count = home_page.get_cart_badge_count()

        assert cart_count == "2", f"Expected '2' items in cart, but got {cart_count}"
        print("✅ Cart badge correctly shows 2 item.")