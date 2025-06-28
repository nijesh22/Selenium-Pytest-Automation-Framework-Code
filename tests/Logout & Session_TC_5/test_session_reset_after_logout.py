import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestSessionResetAfterLogout(BaseTest):
    def test_session_reset_after_logout(self,home_page,login_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.open_menu_and_logout()

        login_page.verify_url("https://www.saucedemo.com/" , "URL")

        self.driver.get("https://www.saucedemo.com/inventory.html")

        assert login_page.get_session_error_message() == "Epic sadface: You can only access '/inventory.html' when you are logged in.", \
            "❌ Session did not reset — was able to access inventory without being logged in"
        log.info("✅ Session reset working as expected. Protected page can't be accessed after logout.")