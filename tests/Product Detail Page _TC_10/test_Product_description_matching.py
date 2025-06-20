import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProductDetailPage import ProductDetailPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestProductDescriptionMatching:
    def test_product_description_matching(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        product_detail_page = ProductDetailPage(self.driver, wait)

        product_count = len(home_page.get_product_desc_elements())

        for i in range(product_count):
            product_desc = home_page.get_product_desc_by_index(i)
            home_page.click_product_by_index(i)

            product_desc_details_page = product_detail_page.get_product_desc_text()

            assert product_desc == product_desc_details_page, f"❌ Mismatch! Expected: {product_desc}, Got: {product_desc_details_page}"
            log.info(f"✅ {product_desc} ✅ Both description are Correctly Displayed.")

            self.driver.back()