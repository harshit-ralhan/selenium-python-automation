import pytest
from pages.login_page import LoginPage
from utils.data_loader import load_test_data
test_data = load_test_data()
@pytest.mark.parametrize("user",[
  test_data["valid_user"],
  test_data["locked_user"],
  test_data["invalid_user"]
  ])
def test_login_parametrized(driver, user):
    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])