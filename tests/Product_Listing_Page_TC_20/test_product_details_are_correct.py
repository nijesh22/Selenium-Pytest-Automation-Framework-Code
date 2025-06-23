import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestProductDetailsAreCorrect:
    def test_product_details_are_correct(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        products = home_page.get_all_products()

        assert len(products) > 0, "❌ No products found!"

        for index, product in enumerate(products):
            info = home_page.get_product_info(product)

            log.info(f"\n🛍️ Checking Product #{index + 1}")
            log.info(f"✅ Name: {info['name']}")
            log.info(f"✅ Description: {info['description']}")
            log.info(f"✅ Price: {info['price']}")
            log.info(f"✅ Button Text: {info['button']}")

            assert info['name'], f"❌ Product {index + 1} name is empty!"
            assert info['description'], f"❌ Product {index + 1} description is missing!"
            assert "$" in info['price'], f"❌ Product {index + 1} price doesn't contain '$'"
            assert "Add to cart" in info['button'], f"❌ Button for product {index + 1} is not 'Add to cart'"