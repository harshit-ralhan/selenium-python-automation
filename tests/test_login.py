import pytest
from pages.login_page import LoginPage
from utils.data_loader import load_test_data
test_data = load_test_data()
@pytest.mark.parametrize("user",[
  test_data["valid_user"],
  test_data["locked_user"],
  test_data["invalid_user"]
  ], ids=[
      "valid_user",
      "locked_user",
      "invalid_user"
  ]

  )
def test_login(driver, user, logger):
    logger.info(f"Starting login test for {user['username']}")
    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])
    logger.info(f"Finished login test for {user['username']}")