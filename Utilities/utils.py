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
