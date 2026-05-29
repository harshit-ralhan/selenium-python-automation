import pytest
from pages.login_page import LoginPage
# from conftest import config
# source = config["data_source"]
import os
from utils.data_loader import load_test_data
source = os.getenv("DATA_SOURCE","json")
test_data = load_test_data(source=source)
@pytest.mark.parametrize("user",test_data,ids=[data["username"] for data in test_data])
def test_login(driver, user, logger):
    logger.info(f"Starting login test for {user['username']}")
    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])
    logger.info(f"Finished login test for {user['username']}")