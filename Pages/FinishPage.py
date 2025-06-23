from selenium.webdriver.common.by import By

from Base.Base_driver import BaseDriver


class FinishPage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)


    # ---------- Locators ----------
    _finish_btn = (By.ID, "finish")
    _thank_you_msg = (By.CLASS_NAME, "complete-header")
    _back_home_btn = (By.ID, "back-to-products")

    # ---------- Actions ----------

    def click_finish(self):
        self.driver.find_element(*self._finish_btn).click()

    def click_back_home_button(self):
        self.driver.find_element(*self._back_home_btn).click()

    # ---------- Getters ----------

    def thankyou_message(self):
        return self.driver.find_element(*self._thank_you_msg).text

    # ---------- Validations ----------

    def is_on_checkout_complete(self):
        return "checkout-complete" in self.driver.current_url
