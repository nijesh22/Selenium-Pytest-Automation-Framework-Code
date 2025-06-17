from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def click_continue(self):
        self.driver.find_element(By.ID, "continue").click()

    def get_current_url(self):
        return self.driver.current_url

    def is_on_step_one(self):
        return "checkout-step-one" in self.driver.current_url

    def first_last_zip_validation(self, first_name_step_one_page, last_name_step_one_page,zip_step_one_page):
        # first name
        first_name = self.driver.find_element(By.ID, "first-name")
        first_name.send_keys(first_name_step_one_page)

        # last name
        last_name = self.driver.find_element(By.ID, "last-name")
        last_name.send_keys(last_name_step_one_page)

        # zip
        zip = self.driver.find_element(By.ID, "postal-code")
        zip.send_keys(zip_step_one_page)

    def fname_lname_zipcode_error_message(self):

        return self.driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')

    def cancel(self):
        self.driver.find_element(By.ID, "cancel").click()

    def get_first_name_placeholder(self):
        element = self.driver.find_element(By.CSS_SELECTOR, '[data-test="firstName"]')
        return element.get_attribute("placeholder")

    def get_last_name_placeholder(self):
        element = self.driver.find_element(By.CSS_SELECTOR, '[data-test="lastName"]')
        return element.get_attribute("placeholder")

    def get_postal_code_placeholder(self):
        element = self.driver.find_element(By.CSS_SELECTOR, '[data-test="postalCode"]')
        return element.get_attribute("placeholder")
