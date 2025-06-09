from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def click_menu(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()

    def click_logout(self):
        # Wait for the logout link to be clickable
        logout_link = self.wait.until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_link.click()

    def get_all_products(self):
        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item")

    def add_backpack_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def get_cart_badge_count(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        except:
            return "0"  # If badge element not found, cart is empty

    def add_backpack_and_bike_light(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    def remove_backpack_from_cart(self):
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()