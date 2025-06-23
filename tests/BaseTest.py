from selenium.webdriver.support.ui import WebDriverWait
from Pages.LoginPage import LoginPage
from Utilities.utils import Utils


class BaseTest:

    def get_wait(self, driver, timeout=10):
        return WebDriverWait(driver, timeout)

    def login_to_saucedemo(self, driver, username="standard_user", password="secret_sauce"):
        wait = self.get_wait(driver)
        login_page = LoginPage(driver, wait)
        login_page.swag_labs_loginIsvalid(username, password)
        login_page.swag_labs_login_button()
        return wait
