import pytest
from utils.data_loader import load_test_data
test_data = load_test_data()

@pytest.mark.parametrize("checkout_info",[
  test_data['valid_check_out_info']
])
def test_checkout_valid_info(login_page, cart_page, checkout_page, checkout_info):
  # login
  login_page.login("standard_user", "secret_sauce")
  #add item to cart
  cart_page.add_item_to_cart("Sauce Labs Backpack")
  # checkout
  checkout_page.navigate_to_checkout_page()
  checkout_page.enter_shipping_info(checkout_info["first_name"], checkout_info["last_name"],
  checkout_info["zip"])
  
  checkout_page.submit_order()
  # verify confirmation
  assert "Thank you for your order!" in checkout_page.get_confirmation_message()

@pytest.mark.parametrize("checkout_info",[
  test_data['invalid_check_out_info_1'],
  test_data['invalid_check_out_info_2'],
  test_data['invalid_check_out_info_3']
])
def test_checkout_invalid_info(login_page, cart_page, checkout_page,checkout_info):
  #login
  login_page.login("standard_user", "secret_sauce")
  # add item to cart
  cart_page.add_item_to_cart("Sauce Labs Backpack")
  # checkout with missing info
  checkout_page.navigate_to_checkout_page()
  checkout_page.enter_shipping_info(checkout_info["first_name"], checkout_info["last_name"],
  checkout_info["zip"])
  # verify error message
  assert "Error" in checkout_page.get_error_message()