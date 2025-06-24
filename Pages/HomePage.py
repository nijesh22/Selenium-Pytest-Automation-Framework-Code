from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from Base.Base_driver import BaseDriver


class HomePage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # ---------- Locators ----------
    _menu_btn = (By.ID, "react-burger-menu-btn")
    _logout_link = (By.ID, "logout_sidebar_link")
    _product_items = (By.CLASS_NAME, "inventory_item")
    _cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    _sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    _cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    _footer_text = (By.CLASS_NAME, "footer_copy")

    _product_names = (By.CLASS_NAME, "inventory_item_name")
    _product_prices = (By.CLASS_NAME, "inventory_item_price")
    _product_descs = (By.CLASS_NAME, "inventory_item_desc")
    _product_images = (By.XPATH, "//div[@class='inventory_item_img']//img")

    _backpack_add_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    _bike_light_add_btn = (By.ID, "add-to-cart-sauce-labs-bike-light")
    _backpack_remove_btn = (By.ID, "remove-sauce-labs-backpack")
    _backpack_link = (By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']")
    _backpack_image = (By.XPATH, "//img[@alt='Sauce Labs Backpack']")
    _click_cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")

        # Sidebar
    _about_link = (By.ID, "about_sidebar_link")
    _all_items_link = (By.ID, "inventory_sidebar_link")
    _close_menu_btn = (By.ID, "react-burger-cross-btn")

        # Footer Social
    _twitter = (By.XPATH, "//a[normalize-space()='Twitter']")
    _facebook = (By.XPATH, "//a[normalize-space()='Facebook']")
    _linkedin = (By.XPATH, "//a[normalize-space()='LinkedIn']")

    # ---------- Actions ----------

    def click_menu(self):
        self.driver.find_element(*self._menu_btn).click()

    def click_logout(self):
        # Wait for the logout link to be clickable
        logout_link = self.wait.until(
            EC.element_to_be_clickable(self._logout_link)
        )
        logout_link.click()

    def add_backpack_to_cart(self):
        self.driver.find_element(*self._backpack_add_btn).click()

    def add_backpack_and_bike_light(self):
        self.driver.find_element(*self._backpack_add_btn).click()
        self.driver.find_element(*self._bike_light_add_btn).click()

    def remove_backpack_from_cart(self):
        self.driver.find_element(*self._backpack_remove_btn).click()

    def Sauce_Labs_Backpack_Page_click(self):
        self.driver.find_element(*self._backpack_link).click()

    def Sauce_Labs_Backpack_Image_click(self):
        self.wait.until(EC.element_to_be_clickable(self._backpack_image)).click()

    def click_product_by_index(self, index):
        self.get_product_elements()[index].click()

    def get_homepage_cart_icon_click(self):

        self.wait.until(EC.element_to_be_clickable(self._click_cart_icon)).click()

    def side_menu_about_button(self):
        self.wait.until(EC.element_to_be_clickable(self._about_link)).click()

    def side_menu_Alliteams_button(self):
        self.wait.until(EC.element_to_be_clickable(self._all_items_link)).click()

    def side_menu_close_button(self):
        self.wait.until(EC.element_to_be_clickable(self._close_menu_btn)).click()

    def twitter_footer(self):
        self.wait.until(EC.element_to_be_clickable(self._twitter)).click()

    def facebook_footer(self):
        self.wait.until(EC.element_to_be_clickable(self._facebook)).click()

    def linkedin_footer(self):
        self.wait.until(EC.element_to_be_clickable(self._linkedin)).click()


    # ---------- Getters ----------

    def get_all_products(self):
        self.wait.until(EC.presence_of_all_elements_located(self._product_items))
        return self.driver.find_elements(self._product_items)

    def get_cart_badge_count(self):
        try:
            return self.driver.find_element(*self._cart_badge).text
        except:
            return "0"  # If badge element not found, cart is empty

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



    def select_sort_option(self, visible_text):
        dropdown = Select(self.driver.find_element(*self._sort_dropdown ))
        dropdown.select_by_visible_text(visible_text)

    def get_product_names(self):
        name_elements = self.driver.find_elements(*self._product_names )
        return [name.text for name in name_elements]

    def get_product_prices(self):
        price_elements = self.driver.find_elements(*self._product_prices)
        return [float(price.text.replace("$", "")) for price in price_elements]

    def get_product_name_elements(self):
        return self.driver.find_elements(*self._product_names)

    def get_product_images(self):
        return self.driver.find_elements(*self._product_images)


    def get_product_desc(self):
        return self.driver.find_elements(*self._product_descs)

    def get_product_elements(self):
        return self.driver.find_elements(*self._product_names)

    def get_product_name_by_index(self, index):
        return self.get_product_elements()[index].text

    def get_product_price_elements(self):
        return self.driver.find_elements(*self._product_prices)

    def get_product_price_by_index(self, index):
        return self.get_product_price_elements()[index].text

    def get_product_desc_elements(self):
        return self.driver.find_elements(*self._product_descs)

    def get_product_desc_by_index(self, index):
        return self.get_product_desc_elements()[index].text

    def footer_text(self):
        return self.driver.find_element(*self._footer_text).text

    def is_burger_menu_visible(self):
        return self.driver.find_element(*self._menu_btn).is_displayed()

    def resize_window(self, width, height):
        self.driver.set_window_size(width, height)

    def add_backpack_item_and_go_to_cart(self):
        self.add_backpack_to_cart()
        self.get_homepage_cart_icon_click()

    def open_menu_and_logout(self):
        self.click_menu()
        self.click_logout()

    def open_and_close_side_menu(self):
        self.click_menu()
        self.side_menu_close_button()