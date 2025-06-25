import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest

@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestValidateProductNamesVisible(BaseTest):
    def test_validate_product_names_visible(self,home_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        product_names = home_page.get_product_name_elements()

        for product_element in product_names:
            assert product_element.is_displayed(), f"❌ Product '{product_element.text}' is not visible!"
            log.info(f"✅ Product visible: {product_element.text}")
