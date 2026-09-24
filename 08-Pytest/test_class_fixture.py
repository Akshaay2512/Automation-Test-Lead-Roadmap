import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def launch_browser_class(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    driver.maximize_window()

    request.cls.driver = driver

    yield driver

    driver.quit()


@pytest.mark.usefixtures("launch_browser_class")
class Test_login:

    def test_username(self):
        self.driver.find_element(
            By.XPATH, "//input[@name='email']"
        ).send_keys("testuser@gmail.com")

    def test_password(self):
        self.driver.find_element(
            By.XPATH, "//input[@name='pass']"
        ).send_keys("Test@123")
        time.sleep(5)