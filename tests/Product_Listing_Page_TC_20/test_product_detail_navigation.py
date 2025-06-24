import pytest
from Pages.HomePage import HomePage
from Pages.ProductDetailPage import ProductDetailPage
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestProductDetailNavigation(BaseTest):
    def test_product_detail_navigation(self):

        wait = self.login_to_saucedemo(self.driver)

        home_page = HomePage(self.driver, wait)
        home_page.Sauce_Labs_Backpack_Page_click()

        Product_DetailPage = ProductDetailPage(self.driver, wait)
        Product_DetailPage.verify_url("https://www.saucedemo.com/inventory-item.html?id=4" , "URL")
