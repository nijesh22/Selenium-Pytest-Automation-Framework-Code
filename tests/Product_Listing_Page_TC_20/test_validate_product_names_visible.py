import pytest
from selenium.webdriver.support.ui import WebDriverWait
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestValidateProductNamesVisible:
    def test_Validate_Product_Names_Visible(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)

        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        product_names = home_page.get_product_name_elements()

        for product_element in product_names:
            assert product_element.is_displayed(), f"❌ Product '{product_element.text}' is not visible!"
            log.info(f"✅ Product visible: {product_element.text}")
