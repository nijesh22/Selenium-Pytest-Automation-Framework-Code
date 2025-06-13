from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def get_cart_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    def get_cart_product_desc(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_desc").text

    def get_cart_product_price(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text

    def cart_remove_product_cart_page(self):
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    def cart_continue_button_cart_page(self):
        self.driver.find_element(By.ID, "continue-shopping").click()

    def cart_checkout_button_cart_page(self):
        self.driver.find_element(By.ID, "checkout").click()

    def cart_quantity_count_cart_page_element(self):
        return self.driver.find_elements(By.CLASS_NAME, "cart_quantity")

    def cart_quantity_count_cart_page_element_index(self,index):
        return self.cart_quantity_count_cart_page_element()[index].text

    def cart_is_empty_or_not_cart_page_element(self):
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")