from selenium.webdriver.common.by import By

class CartPageLocator:
  # dynamic_add_to_cart_button = 
  shopping_cart_link = (By.XPATH, '//a[@data-test="shopping-cart-link"]')
  checkout_button = (By.XPATH, '//button[text()="Checkout"]')
  pass