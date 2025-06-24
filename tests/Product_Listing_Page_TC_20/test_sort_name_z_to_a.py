import pytest
from selenium.webdriver.support.ui import WebDriverWait
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestSortByName(BaseTest):
    def test_sort_name_z_to_a(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        # log = Utils.customlogger()
        # wait = WebDriverWait(self.driver, 10)
        # login_page = LoginPage(self.driver, wait)
        # login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        # login_page.swag_labs_login_button()


        home_page = HomePage(self.driver, wait)
        home_page.select_sort_option("Name (Z to A)")
        ui_product_names = home_page.get_product_names()
        sorted_desc = sorted(ui_product_names, reverse=True)

        assert ui_product_names == sorted_desc, f"❌ Names not sorted Z-A. Got: {ui_product_names}"
        log.info("✅ Product names are sorted Z-A correctly.")
