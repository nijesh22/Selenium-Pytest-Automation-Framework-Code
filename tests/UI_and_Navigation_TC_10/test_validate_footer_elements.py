import pytest
from Utilities.utils import Utils
from tests.BaseTest import BaseTest


#@pytest.mark.skip(reason="Skipping temporarily – avoids confusion"
@pytest.mark.usefixtures("setup")
class TestValidateFooterElements(BaseTest):
    def test_validate_footer_elements(self,home_page):

        log = Utils.customlogger()
        wait = self.login_to_saucedemo(self.driver)

        home_page.twitter_footer()

        self.driver.switch_to.window(self.driver.window_handles[1])

        home_page.verify_url("https://x.com/saucelabs","Sauce Labs X URL")

        self.driver.switch_to.window(self.driver.window_handles[0])

        home_page.facebook_footer()

        self.driver.switch_to.window(self.driver.window_handles[2])

        home_page.verify_url("https://www.facebook.com/saucelabs", "Sauce Labs Facebook URL")

        self.driver.switch_to.window(self.driver.window_handles[0])

        home_page.linkedin_footer()

        self.driver.switch_to.window(self.driver.window_handles[3])

        home_page.verify_url("https://www.linkedin.com/company/sauce-labs/", "Sauce Labs Linkedin URL")

        self.driver.switch_to.window(self.driver.window_handles[0])

        footer_text = home_page.footer_text()

        assert footer_text == '© 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy', f"❌ Expected  to show ' © 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy ', but got '{footer_text}'"
        log.info("✅ shows the correct footer Text Verification successful.")

