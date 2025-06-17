from selenium.webdriver.common.by import By

class FinishPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def click_finish(self):
        self.driver.find_element(By.ID, "finish").click()

    def thankyou_message(self):
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text

    def click_back_home_button(self):
        self.driver.find_element(By.ID, "back-to-products").click()

    def is_on_checkout_complete(self):
        return "checkout-complete" in self.driver.current_url
