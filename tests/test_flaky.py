import pytest
import random
from selenium import webdriver

def test_flaky_example():
    driver = webdriver.Chrome()
    driver.get("https://example.com")

    # Simulate flakiness: randomly fail
    if random.choice([True, False]):
        driver.quit()
        pytest.fail("Simulated flaky failure")

    driver.quit()
