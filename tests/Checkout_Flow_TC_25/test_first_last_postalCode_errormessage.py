import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckoutPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProductDetailPage import ProductDetailPage


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class Test_first_last_postalCode_errormessage:

    @pytest.mark.parametrize(
        "fname, lname, zipcode,expected_error",
        [
            ("", "ragav","123456","Error: First Name is required" ,),
            ("manu", "", "123456", "Error: Last Name is required"),
            ("manu", "ragav", "", "Error: Postal Code is required"),
            pytest.param("   ", "   ", "   ", "Error: First Name is required",
                         marks=pytest.mark.xfail(reason="Whitespace input validation not implemented")), # Whitespace in all
            pytest.param("manu", "ragav", "@#%", "Error: Postal Code is required",
                         marks=pytest.mark.xfail(reason="Special character validation not implemented")), # # Special chars in postal
        ],
        ids=[
            "Blank first name , filled last name and zipcode",
            "first name , last name blank and zipcode",
            "filled first name , filled last name and black zipcode",
            "Whitespace in all fields",
            "Special characters in postal code"
        ]
    )

    def test_first_last_postalCode_errormessage_1(self,fname,lname,zipcode,expected_error):
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.Sauce_Labs_Backpack_Image_click()
        details_page = ProductDetailPage(self.driver, wait)
        details_page.add_backpack_to_cart_details_page()
        home_page.get_homepage_cart_icon_click()
        Cart_page = CartPage(self.driver, wait)
        Cart_page.cart_checkout_button_cart_page()


        checkout_page = CheckoutPage(self.driver, wait)
        checkout_page.first_last_zip_validation(fname,lname,zipcode)

        checkout_page.click_continue()


        error_name = checkout_page.fname_lname_zipcode_error_message()
        error_text = error_name.text

        # Assertion
        assert error_text == expected_error, f"❌ Expected: '{expected_error}', but got: '{error_text}'"
        print(f"✅ Correct error message displayed: {error_text}")



