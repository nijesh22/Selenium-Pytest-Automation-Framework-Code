import pytest
from selenium.webdriver.support.wait import WebDriverWait
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils


@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestValidateFooterElements:
    def test_validate_footer_elements(self):
        log = Utils.customlogger()
        wait = WebDriverWait(self.driver, 10)
        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        home_page.twitter_footer()

        self.driver.switch_to.window(self.driver.window_handles[1])

        home_page.verify_url("https://x.com/saucelabs","Sauce Labs X URL")

        # current_url = self.driver.current_url
        # expected_url = "https://x.com/saucelabs"
        #
        # if current_url == expected_url:
        #     log.info(f"✅ Correct Sauce Labs X URL: {current_url}")
        # else:
        #     log.error(f"❌ Incorrect Sauce Labs X URL! Expected: {expected_url}, but got: {current_url}")
        #
        # assert current_url == expected_url, f"❌ X URL Expected: {expected_url}, but got: {current_url}"

        self.driver.switch_to.window(self.driver.window_handles[0])

        home_page.facebook_footer()

        self.driver.switch_to.window(self.driver.window_handles[2])

        home_page.verify_url("https://www.facebook.com/saucelabs", "Sauce Labs Facebook URL")

        # current_url = self.driver.current_url
        # expected_url = "https://www.facebook.com/saucelabs"
        #
        # if current_url == expected_url:
        #     log.info(f"✅ Correct Sauce Labs Facebook URL: {current_url}")
        # else:
        #     log.error(f"❌ Incorrect Sauce Labs Facebook URL! Expected: {expected_url}, but got: {current_url}")
        #
        # assert current_url == expected_url, f"❌ Facebook URL Expected: {expected_url}, but got: {current_url}"

        self.driver.switch_to.window(self.driver.window_handles[0])

        home_page.linkedin_footer()

        self.driver.switch_to.window(self.driver.window_handles[3])

        home_page.verify_url("https://www.linkedin.com/company/sauce-labs/", "Sauce Labs Linkedin URL")

        # current_url = self.driver.current_url
        # expected_url = "https://www.linkedin.com/company/sauce-labs/"
        #
        # if current_url == expected_url:
        #     log.info(f"✅ Correct Sauce Labs Linkedin URL: {current_url}")
        # else:
        #     log.error(f"❌ Incorrect Sauce Labs Linkedin URL! Expected: {expected_url}, but got: {current_url}")
        #
        # assert current_url == expected_url, f"❌ Linkedin URL Expected: {expected_url}, but got: {current_url}"

        self.driver.switch_to.window(self.driver.window_handles[0])

        footer_text = home_page.footer_text()

        assert footer_text == '© 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy', f"❌ Expected  to show ' © 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy ', but got '{footer_text}'"
        log.info("✅ shows the correct footer Text Verification successful.")

