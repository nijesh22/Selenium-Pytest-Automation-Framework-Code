import pytest
from selenium.webdriver.support.ui import WebDriverWait
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestAddRemoveAfterSorting(BaseTest):
    def test_add_remove_after_sorting(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        # log = Utils.customlogger()
        # wait = WebDriverWait(self.driver, 10)
        #
        # login_page = LoginPage(self.driver, wait)
        # login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        # login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        descriptions = home_page.get_product_desc()

        for idx, element in enumerate(descriptions , start= 1):
            description_text = element.text.strip()
            log.info(f"Description {idx}: '{description_text}'")
            assert description_text != "", f"❌ Description at index {idx} is empty!"


