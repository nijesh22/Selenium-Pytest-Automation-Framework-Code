import time
from asyncio import wait_for

from selenium.webdriver.common.by import By

from conftest import driver


class LoginPage():
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def swag_labs_loginIsvalid(self , standard_user_login,standard_user_login_password):
        #valid ID
        user_name_valid = self.driver.find_element(By.ID, "user-name")
        user_name_valid.send_keys(standard_user_login)

        #valid Pass
        password_valid = self.driver.find_element(By.ID, "password")
        password_valid.send_keys(standard_user_login_password)

    def swag_labs_login_button(self):
        # login button
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    def login_error_message(self):

        return self.driver.find_element("css selector", "h3[data-test='error']")













