from uistore.cart_page_locator import CartPageLocator
from uistore.checkout_page_locator import CheckoutPageLocator
from time import sleep
class CheckoutPage:
  def __init__(self,driver):
    self.driver = driver
  def navigate_to_checkout_page(self):
    self.driver.find_element(*CartPageLocator.shopping_cart_link).click()
    self.driver.find_element(*CartPageLocator.checkout_button).click()
  def enter_shipping_info(self,first_name, last_name, postal_code):
    self.driver.find_element(*CheckoutPageLocator.first_name_input_field).send_keys(first_name)
    self.driver.find_element(*CheckoutPageLocator.last_name_input_field).send_keys(last_name)
    self.driver.find_element(*CheckoutPageLocator.postal_code_input_field).send_keys(postal_code)
    self.driver.find_element(*CheckoutPageLocator.continue_button).click()
    # sleep(2)
  def submit_order(self):
    self.driver.find_element(*CheckoutPageLocator.finish_button).click()
  def get_confirmation_message(self):
    confirmation_message = self.driver.find_element(*CheckoutPageLocator.confirmation_message_text_locator).text
    return confirmation_message
  def get_error_message(self):
    error_message = self.driver.find_element(*CheckoutPageLocator.error_message_text_locator).text
    return error_message
  def enter_payment_info(self):
    pass