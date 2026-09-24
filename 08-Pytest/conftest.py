import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def launch_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.amazon.com/")
    driver.maximize_window()

    yield driver

    driver.quit()