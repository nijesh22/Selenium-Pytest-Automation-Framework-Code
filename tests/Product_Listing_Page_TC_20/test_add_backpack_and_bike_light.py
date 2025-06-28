import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestAddBackpackAndBikeLight(BaseTest):
    def test_add_backpack_and_bike_light(self,home_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.add_backpack_and_bike_light()
        cart_count = home_page.get_cart_badge_count()

        Utils.assert_cart_badge_count(cart_count, 2, log)
