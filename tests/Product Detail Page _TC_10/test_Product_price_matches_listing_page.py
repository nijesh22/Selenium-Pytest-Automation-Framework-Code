import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProductDetailPage import ProductDetailPage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestProductPriceMatchesListing(BaseTest):
    def test_product_price_matches_listing(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        # log = Utils.customlogger()
        # wait = WebDriverWait(self.driver, 10)
        # login_page = LoginPage(self.driver, wait)
        # login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        # login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        product_detail_page = ProductDetailPage(self.driver, wait)

        product_count = len(home_page.get_product_price_elements())

        for i in range(product_count):
            product_price = home_page.get_product_price_by_index(i)
            home_page.click_product_by_index(i)

            product_price_details_page = product_detail_page.get_product_price()

            assert product_price == product_price_details_page, f"❌ Mismatch! Expected: {product_price}, Got: {product_price_details_page}"
            log.info(f"✅ {product_price} Both Prices are Correctly Displayed.")

            self.driver.back()