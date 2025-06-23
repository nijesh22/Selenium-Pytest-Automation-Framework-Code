from Utilities.utils import Utils


class BaseDriver:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def verify_url(self, expected_url, label="URL"):
        log = Utils.customlogger()
        current_url = self.driver.current_url
        if current_url == expected_url:
            log.info(f"✅ Correct {label}: {current_url}")
        else:
            log.error(f"❌ Incorrect {label}! Expected: {expected_url}, but got: {current_url}")
        assert current_url == expected_url, f"❌ Expected: {expected_url}, but got: {current_url}"

