from selenium.webdriver.common.by import By

class ProductDetailPage:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    # ---------- Locators ----------

    _product_name = (By.CLASS_NAME, "inventory_details_name")
    _product_desc = (By.CLASS_NAME, "inventory_details_desc")
    _product_price = (By.CLASS_NAME, "inventory_details_price")
    _product_image = (By.CLASS_NAME, "inventory_details_img")
    _add_to_cart_btn = (By.ID, "add-to-cart")
    _remove_btn = (By.ID, "remove")
    _back_btn = (By.ID, "back-to-products")
    _desc_data_test = (By.CSS_SELECTOR, '[data-test="inventory-item-desc"]')


    # ---------- Getters ----------
    def get_product_title(self):
        return self.driver.find_element(*self._product_name).text

    def get_product_details_page_images(self):
        return self.driver.find_elements(*self._product_image)

    def get_product_price(self):
        return self.driver.find_element(*self._product_price).text

    def get_product_desc_text(self):
        return self.driver.find_element(*self._desc_data_test).text

    def get_product_details_name(self):
        return self.driver.find_element(*self._product_name).text

    def get_product_details_desc(self):
        return self.driver.find_element(*self._product_desc).text

    def get_product_details_price(self):
        return self.driver.find_element(*self._product_price).text

    # ---------- Actions ----------

    def add_backpack_to_cart_details_page(self):
        self.driver.find_element(*self._add_to_cart_btn).click()

    def remove_backpack_to_cart_details_page(self):
        self.driver.find_element(*self._remove_btn).click()

    def back_to_products_details_page(self):
        self.driver.find_element(*self._back_btn).click()