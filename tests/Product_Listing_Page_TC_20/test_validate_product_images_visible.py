import time
import pytest
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestValidateProductNamesVisible(BaseTest):
    def test_Validate_Product_Image_Visible(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        images = home_page.get_product_images()

        time.sleep(1)
        for img in images:

            Utils.assert_image_is_loaded(self.driver, img, log, label="Product image")

