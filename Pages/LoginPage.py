from selenium.webdriver.common.by import By

from Base.Base_driver import BaseDriver


class LoginPage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # ---------- Locators ----------

    _username_input = (By.ID, "user-name")
    _password_input = (By.ID, "password")
    _login_button = (By.ID, "login-button")
    _error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    # ---------- Actions ----------

    def swag_labs_loginIsvalid(self , standard_user_login,standard_user_login_password):
        #valid ID
        user_name_valid = self.driver.find_element(*self._username_input)
        user_name_valid.send_keys(standard_user_login)

        #valid Pass
        password_valid = self.driver.find_element(*self._password_input)
        password_valid.send_keys(standard_user_login_password)

    def swag_labs_login_button(self):
        # login button
        login_button = self.driver.find_element(*self._login_button)
        login_button.click()

    # ---------- Getters ----------

    def login_error_message(self):
        return self.driver.find_element(*self._error_message)

    def get_session_error_message(self):
        return self.driver.find_element(*self._error_message).text













