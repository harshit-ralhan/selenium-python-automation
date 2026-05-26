from selenium.webdriver.common.by import By
from uistore.inventory_page_locator import InventoryPageLocator
from selenium.webdriver.support.ui import Select
class InventoryPage:
  def __init__(self, driver):
    self.driver = driver
    self.cart_button = (By.ID, "shopping_cart_container")
  def go_to_cart(self):
    self.driver.find_element(*self.cart_button).click()
  def get_all_item_names(self):
    all_item_names_array = self.driver.find_elements(*InventoryPageLocator.dynamic_item_name)
    return all_item_names_array
  def select_sorting_by_value(self,sorting_value):
    sorting_dropdown_web_element = self.driver.find_element(*InventoryPageLocator.sorting_dropdown)
    select = Select(sorting_dropdown_web_element)
    select.select_by_value(sorting_value)
  def get_item_names_with_prices(self):
    names = self.driver.find_elements(*InventoryPageLocator.dynamic_item_name)
    price = self.driver.find_elements(*InventoryPageLocator.dynamic_item_price)
    items = []
    for n,p in zip(names, price):
      price_number = float(p.text.replace("$", ""))
      items.append({"name":n.text, "price":price_number})
    return items