import pytest
from selenium.webdriver.support.ui import WebDriverWait
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestValidateNoDuplicateProducts:
    def test_validate_no_duplicate_Products(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)

        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        product_names = home_page.get_product_names()

        product_names_set = set(product_names)

        assert len(product_names) == len(product_names_set), "❌ Duplicate product names found!"

        log.info("✅ No duplicate products found.")