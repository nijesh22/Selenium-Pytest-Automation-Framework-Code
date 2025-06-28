import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")

class TestAddToCartRapidly(BaseTest):

    def test_add_to_cart_rapidly_using_loop(self,home_page):

        log = Utils.customlogger()
        wait =  self.login_to_saucedemo(self.driver)

        for i in range(1,51):
            home_page.add_backpack_item_and_go_to_cart()
            self.driver.back()

            try:
                home_page.remove_backpack_from_cart()
            except:
                log.error(f" Remove button not found in round {i}")

            home_page.verify_url("https://www.saucedemo.com/inventory.html", "URL")