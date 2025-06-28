import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestRemoveProductToCartFromDetailPage(BaseTest):
    def test_remove_product_to_cart_from_detail_page(self,home_page,product_details_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.Sauce_Labs_Backpack_Image_click()

        product_details_page.add_backpack_to_cart_details_page()

        cart_count = home_page.get_cart_badge_count()

        Utils.assert_cart_badge_count(cart_count, 1, log)

        product_details_page.remove_backpack_to_cart_details_page()

        cart_count_after_removal = home_page.get_cart_badge_count()

        Utils.assert_cart_badge_count(cart_count_after_removal, 0, log)