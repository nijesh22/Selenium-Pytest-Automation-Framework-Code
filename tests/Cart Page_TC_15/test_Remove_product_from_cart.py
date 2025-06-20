import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestRemoveProductFromCart:
    def test_remove_product_from_cart(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_to_cart()
        home_page.get_homepage_cart_icon_click()

        cart_page = CartPage(self.driver, wait)
        cart_page.cart_remove_product_cart_page()
        cart_count_after_removal = home_page.get_cart_badge_count()
        assert cart_count_after_removal == '0', f"❌ Expected cart badge to show '0', but got '{cart_count_after_removal}'"
        log.info("✅ Cart badge correctly shows 0 item in details page.")