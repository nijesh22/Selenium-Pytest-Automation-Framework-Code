#pytest -s --browser=chrome --url=https://www.saucedemo.com --html=Reports/report.html --self-contained-html


import os
import base64
import tempfile
from datetime import datetime
import pytest
import pytest_html
from pytest_html import extras
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

driver = None


@pytest.fixture(autouse=True)
def setup(request, browser, url):
    global driver
    if browser == "chrome":
        chrome_opt = webdriver.ChromeOptions()
        temp_profile_dir = tempfile.mkdtemp()
        chrome_opt.add_argument(f"--user-data-dir={temp_profile_dir}")
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,  # "data breach" warning
            "safeBrowse.enabled": False,
            "autofill.enabled": False
        }
        chrome_opt.add_experimental_option("prefs", prefs)
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_opt)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)

    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        if report.failed:
            root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            reports_dir = os.path.join(root_dir, "Reports")
            screenshots_dir = os.path.join(reports_dir, "screenshots")

            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = report.nodeid.replace("::", "").replace("/", "").replace("\\", "_") + ".png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver = getattr(item.cls, "driver", None)
            if driver:
                try:
                    print(f"Capturing screenshot at: {file_path}")
                    driver.get_screenshot_as_file(file_path)
                    print(f"Screenshot saved to: {file_path}")

                    if os.path.exists(file_path):
                        with open(file_path, "rb") as f:
                            screenshot_data = f.read()
                            base64_screenshot = base64.b64encode(screenshot_data).decode('utf-8')

                        html = f'''<div>
                            <img src="data:image/png;base64,{base64_screenshot}" 
                                 alt="Screenshot" 
                                 style="width:100%; max-width:800px; height:auto; border:1px solid #ddd; border-radius:4px;" 
                                 onclick="window.open(this.src)" 
                                 title="Click to open full size" />
                        </div>'''

                        extra.append(extras.html(html))
                        print(f"Screenshot embedded in HTML report")

                except Exception as e:
                    print(f"Error capturing screenshot: {e}")

                    extra.append(extras.html(f'<div style="color: red;">Failed to capture screenshot: {str(e)}</div>'))
            else:
                print("Driver not available to capture screenshot.")
                extra.append(extras.html('<div style="color: orange;">Driver not available for screenshot</div>'))

    report.extras = extra