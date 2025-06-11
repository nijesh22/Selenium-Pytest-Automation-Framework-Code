import pytest
from selenium.webdriver.support.ui import WebDriverWait
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

@pytest.mark.skip(reason="Skipping temporarily – avoids confusion")
@pytest.mark.usefixtures("setup")
class TestAddRemoveAfterSorting:
    def test_AddRemove_after_sorting(self):
        wait = WebDriverWait(self.driver, 10)

        login_page = LoginPage(self.driver, wait)
        login_page.swag_labs_loginIsvalid("standard_user", "secret_sauce")
        login_page.swag_labs_login_button()

        home_page = HomePage(self.driver, wait)
        descriptions = home_page.get_product_desc()

        for idx, element in enumerate(descriptions , start= 1):
            description_text = element.text.strip()
            print(f"Description {idx}: '{description_text}'")
            assert description_text != "", f"❌ Description at index {idx} is empty!"


