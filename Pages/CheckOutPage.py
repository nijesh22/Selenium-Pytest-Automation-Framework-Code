from selenium.webdriver.common.by import By

from Base.Base_driver import BaseDriver


class CheckoutPage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # ---------- Locators ----------

    _first_name_input = (By.ID, "first-name")
    _last_name_input = (By.ID, "last-name")
    _postal_code_input = (By.ID, "postal-code")
    _continue_btn = (By.ID, "continue")
    _cancel_btn = (By.ID, "cancel")
    _error_msg = (By.CSS_SELECTOR, '[data-test="error"]')
    _first_name_placeholder = (By.CSS_SELECTOR, '[data-test="firstName"]')
    _last_name_placeholder = (By.CSS_SELECTOR, '[data-test="lastName"]')
    _postal_code_placeholder = (By.CSS_SELECTOR, '[data-test="postalCode"]')

    # ---------- Actions ----------

    def first_last_zip_validation(self, first_name_step_one_page, last_name_step_one_page,zip_step_one_page):
        # first name
        first_name = self.driver.find_element(*self._first_name_input)
        first_name.send_keys(first_name_step_one_page)

        # last name
        last_name = self.driver.find_element(*self._last_name_input)
        last_name.send_keys(last_name_step_one_page)

        # zip
        zip = self.driver.find_element(*self._postal_code_input)
        zip.send_keys(zip_step_one_page)

    def click_continue(self):
        self.driver.find_element(*self._continue_btn).click()

    def cancel(self):
        self.driver.find_element(*self._cancel_btn).click()

    # ---------- Getters ----------

    def get_current_url(self):
        return self.driver.current_url

    def fname_lname_zipcode_error_message(self):
        return self.driver.find_element(*self._error_msg)


    def get_first_name_placeholder(self):
        element = self.driver.find_element(*self._first_name_placeholder)
        return element.get_attribute("placeholder")

    def get_last_name_placeholder(self):
        element = self.driver.find_element(*self._last_name_placeholder)
        return element.get_attribute("placeholder")

    def get_postal_code_placeholder(self):
        element = self.driver.find_element(*self._postal_code_placeholder)
        return element.get_attribute("placeholder")

    # ---------- Validations ----------

    def is_on_step_one(self):
        return "checkout-step-one" in self.driver.current_url