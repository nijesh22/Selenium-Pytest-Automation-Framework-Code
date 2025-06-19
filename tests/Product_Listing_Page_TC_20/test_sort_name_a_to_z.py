import pytest
from selenium.webdriver.support.ui import WebDriverWait
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestSortByName:
    def test_sort_name_a_to_z(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)


        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()


        home_page = HomePage(self.driver, wait)
        home_page.select_sort_option("Name (A to Z)")
        ui_product_names = home_page.get_product_names()
        sorted_names = sorted(ui_product_names)

        assert ui_product_names == sorted_names, f"❌ Names not sorted A-Z. Got: {ui_product_names}"
        log.info("✅ Product names are sorted A-Z correctly.")
