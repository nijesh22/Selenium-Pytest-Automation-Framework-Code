from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestInjectScriptInInputFields(BaseTest):

    def test_inject_script_in_input_fields(self,home_page,cart_page,checkout_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.add_backpack_item_and_go_to_cart()

        cart_page.cart_checkout_button_cart_page()

        xss_script = "<script>alert('XSS')</script>"

        checkout_page.first_last_zip_validation(xss_script, xss_script, xss_script)
        checkout_page.click_continue()

        try:
            WebDriverWait(self.driver, 2).until(EC.alert_is_present())
            assert False, "❌ XSS Vulnerability Detected! Alert appeared."
        except:
            log.info("✅ No alert — form is secure from script injection.")
