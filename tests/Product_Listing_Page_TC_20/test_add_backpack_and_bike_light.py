import pytest
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestAddBackpackAndBikeLight(BaseTest):
    def test_add_backpack_and_bike_light(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_and_bike_light()
        cart_count = home_page.get_cart_badge_count()

        assert cart_count == "2", f"Expected '2' items in cart, but got {cart_count}"
        log.info("✅ Cart badge correctly shows 2 item.")