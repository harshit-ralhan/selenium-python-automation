from selenium.webdriver.common.by import By

class InventoryPage:
  def __init__(self, driver):
    self.driver = driver
    self.cart_button = (By.ID, "shopping_cart_container")
  def go_to_cart(self):
    self.driver.find_element(*self.cart_button).click()