# import pytest
# from pages.login_page import LoginPage

# def test_valid_login(driver):
#     driver.get("https://www.saucedemo.com/")
#     login_page = LoginPage(driver)
#     login_page.login("standard_user", "secret_sauce")
#     assert "inventory" in driver.current_url

# def test_invalid_login(driver):
#     driver.get("https://www.saucedemo.com/")
#     login_page = LoginPage(driver)
#     login_page.login("wrong_user", "wrong_pass")
#     error_message = driver.find_element("css selector", "h3[data-test='error']").text
#     assert "Username and password do not match" in error_message


import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password,expected",[
  ("standard_user", "secret_sauce", True), #valid
  ("locked_out_user", "secret_sauce", False), #locked account
  ("wrong_user", "wrong_pass", False) #invalid creds
])
def test_login(driver, username, password, expected):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login(username, password)
    if expected:
        assert "inventory" in driver.current_url
    else:
        error_message = driver.find_element("css selector", "h3[data-test='error']").text
        assert error_message != ""