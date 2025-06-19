import time
from turtledemo.penrose import start

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.CartPage import CartPage
from Pages.CheckOutOverview import CheckOutOverview
from Pages.CheckOutPage import CheckoutPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProductDetailPage import ProductDetailPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class test_verify_product_list_matches_cart_overview:
    def test_verify_product_list_matches_cart_overview_1(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_to_cart()
        home_page.Sauce_Labs_Backpack_Image_click()
        product_detail_page = ProductDetailPage(self.driver, wait)

        product_details_name = product_detail_page.get_product_details_name()
        product_details_desc = product_detail_page.get_product_details_desc()
        product_details_price = product_detail_page.get_product_details_price()

        home_page.get_homepage_cart_icon_click()
        Cart_page = CartPage(self.driver, wait)
        Cart_page.cart_checkout_button_cart_page()

        checkout_page = CheckoutPage(self.driver, wait)
        checkout_page.first_last_zip_validation("manu", "ragav", "12345")
        checkout_page.click_continue()


        checkout_overview_page = CheckOutOverview(self.driver, wait)
        name = checkout_overview_page.get_overview_product_name()
        desc = checkout_overview_page.get_overview_product_desc()
        price = checkout_overview_page.get_overview_product_price()

        assert product_details_name == name, f"❌ Mismatch! Expected: {product_details_name}, Got: {name}"
        log.info(f"✅ {name} ✅ name correctly displayed.")

        assert product_details_desc == desc, f"❌ Mismatch! Expected: {product_details_desc}, Got: {desc}"
        log.info(f"✅ {desc} ✅ desc correctly displayed.")

        assert product_details_price == price, f"❌ Mismatch! Expected: {product_details_price}, Got: {price}"
        log.info(f"✅ {price} ✅ price correctly displayed.")

