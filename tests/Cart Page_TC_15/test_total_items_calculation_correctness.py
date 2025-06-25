import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProductDetailPage import ProductDetailPage
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestTotalItemsCalculationCorrectness(BaseTest):
    def test_total_items_calculation_correctness(self,home_page,cart_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.add_backpack_and_bike_light()

        cart_count = home_page.get_cart_badge_count()

        Utils.assert_cart_badge_count(cart_count, 2, log)

        home_page.get_homepage_cart_icon_click()

        Cart_quantity_count = len(cart_page.cart_quantity_count_cart_page_element())

        total_quantity = 0
        for i in range(Cart_quantity_count):
            qty_text = cart_page.cart_quantity_count_cart_page_element_index(i)
            total_quantity += int(qty_text)

        cart_count_after_removal = int(home_page.get_cart_badge_count())


        assert cart_count_after_removal == total_quantity, f"❌ Didn't Get the Expected Result, but got '{cart_count_after_removal}'"
        log.info(f"✅ Quantity is Correctly Displayed : {total_quantity} items")




