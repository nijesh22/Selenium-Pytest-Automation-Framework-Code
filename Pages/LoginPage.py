import time
from asyncio import wait_for

from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def swag_labs_loginIsvalid(self , standard_user_login):
        input_field = self.driver.find_element(By.ID, "user-name")
        input_field.send_keys(standard_user_login)
        time.sleep(3)



