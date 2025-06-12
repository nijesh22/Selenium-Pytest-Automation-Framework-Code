from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProductDetailPage:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def get_product_title(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_name").text

    def get_product_details_page_images(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_details_img")

    def add_backpack_to_cart_details_page(self):
        self.driver.find_element(By.ID, "add-to-cart").click()

    def remove_backpack_to_cart_details_page(self):
        self.driver.find_element(By.ID, "remove").click()

    def back_to_products_details_page(self):
        self.driver.find_element(By.ID, "back-to-products").click()

    def get_product_price(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_price").text

    def get_product_desc_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-test="inventory-item-desc"]').text
