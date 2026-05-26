from selenium.webdriver.common.by import By
class InventoryPageLocator:
  dynamic_item_name = (By.XPATH,'//div[@data-test="inventory-item-name"]')
  dynamic_item_price = (By.XPATH, '//div[@data-test="inventory-item-price"]')
  sorting_dropdown = (By.XPATH, '//select[@class="product_sort_container"]')