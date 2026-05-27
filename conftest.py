import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.options import Options as FireFoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver import Edge
BASE_URL = "https://www.saucedemo.com/"
@pytest.fixture(scope="function",params=["chrome","edge","firefox"])
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--incognito")
        from selenium.webdriver import Chrome
        driver = Chrome(options=options)
    elif request.param == "firefox":
        options = FireFoxOptions()
        options.add_argument("-private")
        from selenium.webdriver import Firefox
        driver = Firefox(options=options)
    elif request.param == "edge":
        options = EdgeOptions()
        options.add_argument("--inprivate")
        driver = Edge(options=options)
    elif request.param == "brave":
        options = ChromeOptions()
        options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        options.add_argument("--incognito")
        driver = Chrome(options=options)
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

@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot(f"reports/{item.name}.png")