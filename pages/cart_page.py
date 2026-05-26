from selenium.webdriver.common.by import By
class CartPage:
  def __init__(self,driver):
    self.driver = driver
  def add_item_to_cart(self,item_name):
    path_of_add_to_cart_button = f"//div[text()='{item_name}']/parent::a/parent::div/following-sibling::div/button"
    # print(f"path is ${path_of_add_to_cart_button}")
    locator = (By.XPATH, path_of_add_to_cart_button)
    add_to_cart_button_web_element = self.driver.find_element(*locator)
    add_to_cart_button_web_element.click()
  def remove_item_from_cart(self):
    pass
  def get_cart_items(self):
    pass
  def accept_password_alert(self):
    self.driver.switch_to.alert.accept()