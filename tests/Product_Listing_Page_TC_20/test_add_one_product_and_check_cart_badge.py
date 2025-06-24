import pytest
from Pages.HomePage import HomePage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestAddOnProductAndCheckCartBadge(BaseTest):
    def test_add_one_product_and_check_cart_badge(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_to_cart()
        cart_count = home_page.get_cart_badge_count()

        assert cart_count == '1' , f"❌ Expected cart badge to show '1', but got '{cart_count}'"
        log.info("✅ Cart badge correctly shows 1 item.")
