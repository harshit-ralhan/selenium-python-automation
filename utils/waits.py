from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
DEFAULT_TIMEOUT = 10
def wait_for_element_visible(driver, locator, timeout=DEFAULT_TIMEOUT):
  # Wait until element is visible on the page
  return WebDriverWait(driver, timeout).until(
    EC.visibility_of_element_located(locator)
  )
def wait_for_element_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
  # Wait until element is clickable
  return WebDriverWait(driver, timeout).until(
    EC.element_to_be_clickable(locator)
  )
def wait_for_element_present(driver, locator, timeout=DEFAULT_TIMEOUT):
  # Wait until element is present in DOM
  return WebDriverWait(driver,timeout).until(
    EC.presence_of_element_located(locator)
  )