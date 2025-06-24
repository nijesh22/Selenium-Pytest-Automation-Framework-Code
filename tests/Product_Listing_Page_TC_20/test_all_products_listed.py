import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestAllProductsListed(BaseTest):
    def test_all_products_listed(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        # log = Utils.customlogger()
        # wait = WebDriverWait(self.driver, 10)
        # login_page = LoginPage(self.driver, wait)
        # login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        # login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        product_list = home_page.get_all_products()

        log.info(" Products found on page:")
        for product in product_list:
            print(" -", product.text)  # Add .text to see what's inside each product

        assert len(product_list) == 6, f"❌ Expected 6 products, but found {len(product_list)}"
        log.info("✅ All 6 products are found.")
