from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # ---------- Locators ----------
    _product_name = (By.CLASS_NAME, "inventory_item_name")
    _product_desc = (By.CLASS_NAME, "inventory_item_desc")
    _product_price = (By.CLASS_NAME, "inventory_item_price")
    _remove_btn = (By.ID, "remove-sauce-labs-backpack")
    _continue_btn = (By.ID, "continue-shopping")
    _checkout_btn = (By.ID, "checkout")
    _cart_quantity = (By.CLASS_NAME, "cart_quantity")
    _cart_items = (By.CLASS_NAME, "cart_item")

    # ---------- Getters ----------

    def get_cart_product_name(self):
        return self.driver.find_element(*self._product_name).text

    def get_cart_product_desc(self):
        return self.driver.find_element(*self._product_desc).text

    def get_cart_product_price(self):
        return self.driver.find_element(*self._product_price).text

    def cart_quantity_count_cart_page_element(self):
        return self.driver.find_elements(*self._cart_quantity)

    def cart_quantity_count_cart_page_element_index(self,index):
        return self.cart_quantity_count_cart_page_element()[index].text

    def cart_is_empty_or_not_cart_page_element(self):
        return self.driver.find_elements(*self._cart_items)

    # ---------- Actions ----------

    def cart_remove_product_cart_page(self):
        self.driver.find_element(*self._remove_btn).click()

    def cart_continue_button_cart_page(self):
        self.driver.find_element(*self._continue_btn).click()

    def cart_checkout_button_cart_page(self):
        self.driver.find_element(*self._checkout_btn).click()

    # ----------DOM Modification----------

    def change_cart_price_from_DOM(self,new_price="$10000.00"):
        self.driver.execute_script(f"document.querySelector('.inventory_item_price').textContent = '{new_price}';")