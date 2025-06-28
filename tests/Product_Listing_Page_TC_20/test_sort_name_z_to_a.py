import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestSortByName(BaseTest):
    def test_sort_name_z_to_a(self,home_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.select_sort_option("Name (Z to A)")
        ui_product_names = home_page.get_product_names()
        sorted_name = sorted(ui_product_names, reverse=True)

        Utils.assert_list_sorted(ui_product_names, sorted_name, "Product Name Z-A", log)

