import time
import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestProductDetailsImages(BaseTest):
    def test_product_details_images(self,home_page,product_details_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        product_count = len(home_page.get_product_elements())
        for i in range(product_count):
            home_page.click_product_by_index(i)
            images = product_details_page.get_product_details_page_images()

            time.sleep(1)

            for img in images:

                Utils.assert_image_is_loaded(self.driver, img, log, label="Product image")

                self.driver.back()