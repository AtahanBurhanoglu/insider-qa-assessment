import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import os

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    else:
        raise ValueError("Unsupported browser")

    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.instance.driver if hasattr(item.instance, "driver") else None
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = os.path.join("screenshots", f"{item.name}_failed.png")
            driver.save_screenshot(screenshot_path)
