from selenium.webdriver.common.by import By

class CheckOutOverview:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # ---------- Locators ----------
    _product_name = (By.CLASS_NAME, "inventory_item_name")
    _product_desc = (By.CLASS_NAME, "inventory_item_desc")
    _product_price = (By.CLASS_NAME, "inventory_item_price")
    _item_total = (By.CLASS_NAME, "summary_subtotal_label")
    _tax = (By.CLASS_NAME, "summary_tax_label")
    _total = (By.CLASS_NAME, "summary_total_label")
    _cancel_btn = (By.ID, "cancel")

    # ---------- Getters ----------

    def get_overview_product_name(self):
        return self.driver.find_element(*self._product_name).text


    def get_overview_product_desc(self):
        return self.driver.find_element(*self._product_desc).text


    def get_overview_product_price(self):
        return self.driver.find_element(*self._product_price).text

    def get_item_total(self):
        text = self.driver.find_element(*self._total).text
        return float(text.split("$")[1].strip())

    def get_tax(self):
        text = self.driver.find_element(*self._tax).text
        return float(text.split("$")[1].strip())

    def get_total(self):
        text = self.driver.find_element(*self._total).text
        return float(text.split("$")[1].strip())

    # ---------- Actions ----------

    def click_cancel(self):
        self.driver.find_element(*self._cancel_btn).click()