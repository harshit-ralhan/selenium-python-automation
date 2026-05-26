import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://www.saucedemo.com/"

@pytest.fixture(scope="function",params=["chrome"])
def driver(request):
    if request.param == "chrome":
        options = Options()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = Options()
        options.add_argument("--incognito")
        driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def cart_page(driver):
    return CartPage(driver)

@pytest.fixture
def checkout_page(driver):
    return CheckoutPage(driver)

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot(f"reports/{item.name}.png")