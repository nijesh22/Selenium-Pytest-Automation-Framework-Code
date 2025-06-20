import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProductDetailPage import ProductDetailPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestTotalItemsCalculationCorrectness:
    def test_total_items_calculation_correctness(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.add_backpack_and_bike_light()

        cart_count = home_page.get_cart_badge_count()

        assert cart_count == '2', f"❌ Expected cart badge to show '2', but got '{cart_count}'"
        log.info("✅ Cart badge correctly shows 2 items.")

        home_page.get_homepage_cart_icon_click()

        Cart_page = CartPage(self.driver, wait)

        Cart_quantity_count = len(Cart_page.cart_quantity_count_cart_page_element())

        total_quantity = 0
        for i in range(Cart_quantity_count):
            qty_text = Cart_page.cart_quantity_count_cart_page_element_index(i)
            total_quantity += int(qty_text)

        cart_count_after_removal = int(home_page.get_cart_badge_count())


        assert cart_count_after_removal == total_quantity, f"❌ Didn't Get the Expected Result, but got '{cart_count_after_removal}'"
        log.info(f"✅ Quantity is Correctly Displayed : {total_quantity} items")




