import pytest
import time
def test_checkout_positive(login_page, cart_page, checkout_page):
  #login
  login_page.login("standard_user", "secret_sauce")
  print("logged in successfully")
  # time.sleep(3)
  # cart_page.accept_password_alert()
  #add item to cart
  cart_page.add_item_to_cart("Sauce Labs Backpack")
  print("item added to cart successfully")

# checkout
  checkout_page.navigate_to_checkout_page()
  print("clicked on shopping cart link")

  checkout_page.enter_shipping_info("Harshit", "Ralhan", "411045")
  checkout_page.submit_order()

# verify confirmation
  assert "Thank you for your order!" in checkout_page.get_confirmation_message()

def test_checkout_missing_info(login_page, cart_page, checkout_page):
  #login
  login_page.login("standard_user", "secret_sauce")
  # time.sleep(3)
  # cart_page.accept_password_alert()
  # add item to cart
  cart_page.add_item_to_cart("Sauce Labs Backpack")

  # checkout with missing info
  checkout_page.navigate_to_checkout_page()
  checkout_page.enter_shipping_info("", "Ralhan", "411045")

  # verify error message
  assert "Error" in checkout_page.get_error_message()
