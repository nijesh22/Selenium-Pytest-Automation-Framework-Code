import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestValidateNoDuplicateProducts(BaseTest):
    def test_validate_no_duplicate_products(self,home_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        product_names = home_page.get_product_names()

        product_names_set = set(product_names)

        assert len(product_names) == len(product_names_set), "❌ Duplicate product names found!"

        log.info("✅ No duplicate products found.")