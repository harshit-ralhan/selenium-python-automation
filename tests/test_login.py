import pytest
from pages.login_page import LoginPage
# ----------------------------------------
# from utils.data_loader import load_test_data_json
# test_data = load_test_data_json()
# @pytest.mark.parametrize("user",[
#   test_data["valid_user"],
#   test_data["locked_user"],
#   test_data["invalid_user"]
#   ], ids=[
#       "valid_user",
#       "locked_user",
#       "invalid_user"
#   ]

#   )
# -------------------------------------
# from utils.data_loader import load_test_data_csv
# test_data = load_test_data_csv()
# @pytest.mark.parametrize("user",test_data,ids=[data["username"] for data in test_data])
# -------------------------------------
from utils.data_loader import load_test_data_excel
test_data = load_test_data_excel()
@pytest.mark.parametrize("user", test_data, ids=[d["username"] for d in test_data])
# -------------------------------------
def test_login(driver, user, logger):
    logger.info(f"Starting login test for {user['username']}")
    login_page = LoginPage(driver)
    login_page.login(user["username"], user["password"])
    logger.info(f"Finished login test for {user['username']}")