import inspect
import logging
import sys

class Utils:

    @staticmethod
    def customlogger(log_level=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)

        if not logger.handlers:

            # File handler
            file_handler = logging.FileHandler("automation.log", mode='a', encoding='utf-8')
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(name)s : %(message)s',
                datefmt='%I:%M:%S %p %d-%m-%Y'
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            # Console handler (disable emoji to prevent UnicodeEncodeError)
            console_handler = logging.StreamHandler(sys.stdout)
            console_formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%I:%M:%S %p %d-%m-%Y'
            )
            console_handler.setFormatter(console_formatter)
            logger.addHandler(console_handler)

        return logger

    @staticmethod
    def assert_cart_badge_count(actual_count, expected_count, log):
        assert actual_count == str(expected_count), f"❌ Expected cart badge to show '{expected_count}', but got '{actual_count}'"
        log.info(f"✅ Cart badge correctly shows {expected_count} item(s).")

    @staticmethod
    def assert_cart_is_empty(cart_items,items_count, log):
        assert len(cart_items) == items_count, "❌ Cart is not empty!"
        log.info("✅ Cart is empty.")

    @staticmethod
    def assert_text_match(expected, actual, field_name, log):
        assert actual == expected, f"❌ {field_name} Mismatch! Expected: {expected}, Got: {actual}"
        log.info(f"✅ {expected} | {field_name} is correctly displayed.")

    @staticmethod
    def assert_burger_menu_visible(home_page, log):
        assert home_page.is_burger_menu_visible(), "❌ Burger menu not visible!"
        log.info("✅ Burger menu is visible.")

    @staticmethod
    def assert_text_equals(actual, expected, field_label, log):
        assert actual == expected, f"❌ {field_label} Mismatch! Expected: '{expected}', but got: '{actual}'"
        log.info(f"✅ Correct {field_label} displayed: {actual}")

    @staticmethod
    def assert_placeholder(actual, expected, field_label, log):
        assert actual == expected, f"❌ {field_label} placeholder is incorrect! Expected: '{expected}', Got: '{actual}'"
        log.info(f"✅ {field_label} placeholder is correct: '{actual}'")

    @staticmethod
    def assert_image_is_loaded(driver, image_element, log, label="Product image"):
        assert image_element.is_displayed(), f"❌ {label} is not visible on the page."

        is_loaded = driver.execute_script(
            "return arguments[0].complete && arguments[0].naturalWidth > 0", image_element
        )
        assert is_loaded, f"❌ {label} failed to load: {image_element.get_attribute('src')}"
        log.info(f"✅ {label} loaded successfully: {image_element.get_attribute('alt')}")

    @staticmethod
    def assert_list_sorted(actual_list, expected_list, sort_label, log):
        assert actual_list == expected_list, f"❌ {sort_label} sorting failed! Got: {actual_list}"
        log.info(f"✅ {sort_label} sorting is correct.")

