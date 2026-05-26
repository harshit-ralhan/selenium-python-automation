from selenium.webdriver.common.by import By
class CheckoutPageLocator:
  first_name_input_field = (By.ID,"first-name")
  last_name_input_field = (By.ID,"last-name")
  postal_code_input_field = (By.ID,"postal-code")
  continue_button = (By.ID,"continue")
  finish_button = (By.ID,"finish")
  confirmation_message_text_locator = (By.XPATH, "//h2[text()='Thank you for your order!']")
  error_message_text_locator = (By.XPATH, '//h3[@data-test="error"]')