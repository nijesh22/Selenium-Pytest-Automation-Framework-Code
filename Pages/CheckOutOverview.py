from selenium.webdriver.common.by import By

class CheckOutOverview:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def get_overview_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text


    def get_overview_product_desc(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_desc").text


    def get_overview_product_price(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text