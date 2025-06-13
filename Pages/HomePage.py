from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


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

    def get_product_info(self, product_element):
        name = product_element.find_element(By.CLASS_NAME, "inventory_item_name").text
        description = product_element.find_element(By.CLASS_NAME, "inventory_item_desc").text
        price = product_element.find_element(By.CLASS_NAME, "inventory_item_price").text
        button_text = product_element.find_element(By.TAG_NAME, "button").text

        return {
            "name": name,
            "description": description,
            "price": price,
            "button": button_text
        }

    def Sauce_Labs_Backpack_Page_click(self):
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']").click()

    def Sauce_Labs_Backpack_Image_click(self):
        image_locator = (By.XPATH, "//img[@alt='Sauce Labs Backpack']")
        self.wait.until(EC.element_to_be_clickable(image_locator)).click()

    def select_sort_option(self, visible_text):
        dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        dropdown.select_by_visible_text(visible_text)

    def get_product_names(self):
        name_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [name.text for name in name_elements]

    def get_product_prices(self):
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(price.text.replace("$", "")) for price in price_elements]

    def get_product_name_elements(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    def get_product_images(self):
        return self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_img']//img")


    def get_product_desc(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item_desc")


    def get_product_elements(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    def click_product_by_index(self, index):
        self.get_product_elements()[index].click()

    def get_product_name_by_index(self, index):
        return self.get_product_elements()[index].text

    def get_product_price_elements(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    def get_product_price_by_index(self, index):
        return self.get_product_price_elements()[index].text

    def get_product_desc_elements(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item_desc")

    def get_product_desc_by_index(self, index):
        return self.get_product_desc_elements()[index].text

    def get_homepage_cart_icon_click(self):
        cart_locator = (By.XPATH, "//a[@class='shopping_cart_link']")
        self.wait.until(EC.element_to_be_clickable(cart_locator)).click()



