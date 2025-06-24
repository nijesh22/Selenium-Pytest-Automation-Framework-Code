import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestValidateProductNamesVisible(BaseTest):
    def test_Validate_Product_Image_Visible(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        # log = Utils.customlogger()
        # wait = WebDriverWait(self.driver, 10)
        # login_page = LoginPage(self.driver, wait)
        # login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        # login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        images = home_page.get_product_images()

        time.sleep(1)
        for img in images:
            assert img.is_displayed(), f"❌ Image not visible for product."

            is_loaded = self.driver.execute_script(
                "return arguments[0].complete && arguments[0].naturalWidth > 0", img
            )
            assert is_loaded, f"❌ Product image failed to load: {img.get_attribute('src')}"
            log.info(f"✅ Image loaded correctly: {img.get_attribute('alt')}")

