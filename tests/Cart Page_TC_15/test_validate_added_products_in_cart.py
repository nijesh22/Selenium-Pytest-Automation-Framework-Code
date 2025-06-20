import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProductDetailPage import ProductDetailPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestValidateAddedProductsInCart:
    def test_validate_added_products_in_cart(self):
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

        cart_page = CartPage(self.driver, wait)

        cart_page_name = cart_page.get_cart_product_name()
        cart_page_desc = cart_page.get_cart_product_desc()
        cart_page_price = cart_page.get_cart_product_price()

        assert product_details_name == cart_page_name, f"❌ Mismatch! Expected: {product_details_name}, Got: {cart_page_name}"
        log.info(f"✅ {product_details_name} ✅ Product Name is correctly Displayed.")

        assert product_details_desc == cart_page_desc, f"❌ Mismatch! Expected: {product_details_desc}, Got: {cart_page_desc}"
        log.info(f"✅ {product_details_desc} ✅ Product description is correctly Displayed.")

        assert product_details_price == cart_page_price, f"❌ Mismatch! Expected: {product_details_price}, Got: {cart_page_price}"
        log.info(f"✅ {product_details_price} ✅ Product price is correctly Displayed.")
