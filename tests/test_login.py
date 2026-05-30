from pages.login_page import LoginPage
from utils.data_loader import load_test_data
def pytest_generate_tests(metafunc):
    if "user" in metafunc.fixturenames:
        source = metafunc.config.getoption("--data-source")
        test_data = load_test_data(source=source)
        metafunc.parametrize("user",test_data,ids=[d['username'] for d in test_data])
def test_login(driver,user,logger):
    login_page = LoginPage(driver)
    login_page.login(user["username"],user["password"])