import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProductDetailPage import ProductDetailPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestProductDetailsImages:
    def test_product_details_images(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        product_detail_page = ProductDetailPage(self.driver, wait)
        product_count = len(home_page.get_product_elements())
        for i in range(product_count):
            home_page.click_product_by_index(i)
            images = product_detail_page.get_product_details_page_images()

            time.sleep(1)

            for img in images:
                assert img.is_displayed(), f"❌ Image not visible for product."

                is_loaded = self.driver.execute_script(
                    "return arguments[0].complete && arguments[0].naturalWidth > 0", img
                )
                assert is_loaded, f"❌ Product image failed to load: {img.get_attribute('src')}"
                log.info(f"✅ Image loaded correctly: {img.get_attribute('alt')}")

                self.driver.back()