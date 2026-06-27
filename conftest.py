import os
import time
import json
import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from utils.data_loader import load_test_data

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import Chrome

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver import Edge


with open("config.json") as f:
    config = json.load(f)
    
@pytest.fixture(scope="session")
def app_config():
    return config

BASE_URL = config["BASE_URL"]
# DEFAULT_BROWSER = config["browser"]

from utils.logger import get_logger
my_logger = None
@pytest.fixture(scope="session")
def logger(request):
    browser = request.config.getoption("--browser")    
    data_source = request.config.getoption("--data-source")
    global my_logger, log_file_path
    my_logger, log_file_path = get_logger(browser=browser,data_source=data_source)
    return my_logger
#---------------------------------------
# """
# # For Testing across list of browsers
# @pytest.fixture(scope="function",params=["chrome","firefox","edge"])
# def driver(request):
#     if request.param == "chrome":
#         options = ChromeOptions()
#         options.add_argument("--incognito")
#         driver = Chrome(options=options)
#     elif request.param == "firefox":
#         options = FirefoxOptions()
#         options.add_argument("-private")
#         service = FirefoxService(r"C:\Tools\geckodriver\geckodriver.exe")
#         driver = Firefox(service=service,options=options)
#     elif request.param == "edge":
#         options = EdgeOptions()
#         options.add_argument("--inprivate")
#         service = EdgeService(r"C:\Tools\edgedriver\msedgedriver.exe")
#         driver = Edge(service=service,options=options)
#     driver.maximize_window()
#     driver.get(BASE_URL)
#     yield driver
#     driver.quit()
# """
# ----------------------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action = "store",
        default = "chrome",
        help = "Browser option: chrome, firefox, edge"
    )
    parser.addoption(
        "--data-source",
        action="store",
        default="json",
        help = "Data source option: csv, json, excel"
    )
    parser.addoption(
        "--remote",
        action="store_true",
        help="Run tests on Selenium Grid"
    )
# For testing over single browser provided through BROWSER env i.e environment variable or --browser flag/option i.e through CLI
# """
from selenium import webdriver
@pytest.fixture(scope="function")
def driver(request):
    # browser = os.getenv("BROWSER","chrome")   # Read from environment variable. Given as format $env:BROWSER="edge"
    browser = request.config.getoption("--browser")   # Read from CLI. Given as format --browser=edge or --browser="edge"
    remote = request.config.getoption("--remote")
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--incognito")
        if remote:
            driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                options=options
            )
        else:
            driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("-private")
        if remote:
            driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                options=options
            )
        else:
            service = FirefoxService(r"C:\Tools\geckodriver\geckodriver.exe")
            driver = webdriver.Firefox(service=service,options=options)
    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--inprivate")
        if remote:
            driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                options=options
            )
        else:
            service = EdgeService(r"C:\Tools\edgedriver\msedgedriver.exe")
            driver = webdriver.Edge(service=service,options=options)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()
# """
@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def cart_page(driver):
    return CartPage(driver)

@pytest.fixture
def checkout_page(driver):
    return CheckoutPage(driver)

@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)

@pytest.fixture
def test_data(request):
    source = request.config.getoption("--data-source")
    return load_test_data(source=source)

# Report title which displays options used too
def pytest_html_report_title(report):
    from datetime import datetime
    report.title = f"Checkout Tests - {datetime.now().strftime('%Y-%m-%d')} ({report.config.getoption('--browser')}, {report.config.getoption('--data-source')})"

browser_option = None
data_source_option = None

def pytest_configure(config):
    global browser_option, data_source_option
    browser_option = config.getoption("--browser")
    data_source_option = config.getoption("--data-source")

def pytest_html_results_summary(prefix, summary, postfix):
    import platform
    prefix.extend([f"OS: {platform.system()} {platform.release()}"])
    prefix.extend([f"Browser: {browser_option}"])
    prefix.extend([f"Data Source: {data_source_option}"])

# import platform
# def pytest_configure(config):
#     config._metadata['OS'] = platform.system() + " " + platform.release()
#     config._metadata['Browser'] = config.getoption("--browser")
#     config._metadata['Data Source'] = config.getoption("--data-source")

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            browser = item.config.getoption("--browser")
            data_source = item.config.getoption("--data-source")
            screenshot_folder = f"reports/{browser}_{data_source}/screenshots"
            os.makedirs(screenshot_folder, exist_ok=True)
            screenshot_path = f"{screenshot_folder}/{item.name}_{int(time.time())}.png"
            driver.save_screenshot(screenshot_path)
            my_logger.error(f"Test {item.name} failed. Screenshot saved at {screenshot_path}")
            if hasattr(report, "extra"):
                from pytest_html import extras
                report.extra.append(extras.image(screenshot_path))
                report.extra.append(extras.text(f"Log file: {log_file_path}"))