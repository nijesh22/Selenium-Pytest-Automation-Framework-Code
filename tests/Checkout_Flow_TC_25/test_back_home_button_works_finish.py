import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.CartPage import CartPage
from Pages.CheckOutOverview import CheckOutOverview
from Pages.CheckOutPage import CheckoutPage
from Pages.FinishPage import FinishPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProductDetailPage import ProductDetailPage


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class Test_back_home_button_works_finish:
    def test_back_home_button_works_finish_1(self):
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_to_cart()
        home_page.Sauce_Labs_Backpack_Image_click()

        home_page.get_homepage_cart_icon_click()
        Cart_page = CartPage(self.driver, wait)
        Cart_page.cart_checkout_button_cart_page()

        checkout_page = CheckoutPage(self.driver, wait)
        checkout_page.first_last_zip_validation("manu", "ragav", "12345")
        checkout_page.click_continue()

        finish_page = FinishPage(self.driver, wait)
        finish_page.click_finish()

        finish_page.click_back_home_button()

        current_url = self.driver.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"

        if current_url == expected_url:
            print(f"✅ Correct URL: {current_url}")
        else:
            print(f"❌  Incorrect URL: {expected_url}, but got: {current_url}")

        assert current_url == expected_url, f"❌ URL: Expected: {expected_url}, but got: {current_url}"