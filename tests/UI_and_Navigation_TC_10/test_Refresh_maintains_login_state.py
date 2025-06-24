import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestRefreshMaintainsLoginState(BaseTest):
    def test_refresh_maintains_login_state(self):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        for i in range(1 ,11):
            self.driver.refresh()
            current_url = self.driver.current_url
            expected_url = "https://www.saucedemo.com/inventory.html"

            assert current_url == expected_url, f"❌ URL Expected: {expected_url}, but got: {current_url}"
            log.info(f"successfully refreshed round : {i}")