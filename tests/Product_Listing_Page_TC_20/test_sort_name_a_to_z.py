import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestSortByName(BaseTest):
    def test_sort_name_a_to_z(self,home_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.select_sort_option("Name (A to Z)")
        ui_product_names = home_page.get_product_names()
        sorted_names = sorted(ui_product_names)

        Utils.assert_list_sorted(ui_product_names, sorted_names, "Product Name A-Z", log)

