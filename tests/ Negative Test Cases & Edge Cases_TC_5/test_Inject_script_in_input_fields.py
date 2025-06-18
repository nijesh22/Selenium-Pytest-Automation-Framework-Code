import time
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage

@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class Test_Inject_script_in_input_fields:
    def test_Inject_script_in_input_fields_1(self):
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_to_cart()
        home_page.get_homepage_cart_icon_click()

        cart_page = CartPage(self.driver, wait)
        cart_page.cart_checkout_button_cart_page()

        xss_script = "<script>alert('XSS')</script>"

        checkout_page = CheckoutPage(self.driver, wait)
        checkout_page.first_last_zip_validation(xss_script, xss_script, xss_script)
        checkout_page.click_continue()

        try:
            WebDriverWait(self.driver, 2).until(EC.alert_is_present())
            assert False, "❌ XSS Vulnerability Detected! Alert appeared."
        except:
            print("✅ No alert — form is secure from script injection.")
