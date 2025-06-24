import pytest
from Pages.HomePage import HomePage
from Pages.ProductDetailPage import ProductDetailPage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestAddProductToCartFromDetailPage(BaseTest):
    def test_add_product_to_cart_from_detail_page(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.Sauce_Labs_Backpack_Image_click()
        details_page = ProductDetailPage(self.driver, wait)
        details_page.add_backpack_to_cart_details_page()

        cart_count = home_page.get_cart_badge_count()

        assert cart_count == '1', f"❌ Expected cart badge to show '1', but got '{cart_count}'"
        log.info("✅ Cart badge correctly shows 1 item in details page.")

        details_page.remove_backpack_to_cart_details_page()

        cart_count_after_removal = home_page.get_cart_badge_count()
        assert cart_count_after_removal == '0', f"❌ Expected cart badge to show '0', but got '{cart_count_after_removal}'"
        log.info("✅ Cart badge correctly shows 0 item.")
