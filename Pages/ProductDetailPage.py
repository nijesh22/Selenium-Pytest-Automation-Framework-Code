from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProductDetailPage:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait


