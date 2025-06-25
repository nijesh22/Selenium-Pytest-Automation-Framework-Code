import time
import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestValidateResponsiveLayout(BaseTest):
    def test_validate_responsive_layout(self,home_page):
        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        # Resize to mobile
        home_page.resize_window(375, 667)
        time.sleep(1)

        Utils.assert_burger_menu_visible(home_page, log)

        home_page.open_and_close_side_menu()

        # Resize to desktop
        home_page.resize_window(1366, 768)
        time.sleep(1)
        Utils.assert_burger_menu_visible(home_page, log)

        home_page.open_and_close_side_menu()

        # Resize to tablet
        self.driver.set_window_size(768, 1024)
        time.sleep(1)
        Utils.assert_burger_menu_visible(home_page, log)

        home_page.open_and_close_side_menu()