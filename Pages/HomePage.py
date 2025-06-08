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
