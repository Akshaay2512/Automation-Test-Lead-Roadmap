import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def launch_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get("https://www.facebook.com/")

    return driver


def test_open(launch_browser):
    driver = launch_browser
    print(driver.title)


def test_url(launch_browser):
    driver = launch_browser

    current_url = driver.current_url
    expected_url = "https://www.facebook.com/"

    assert current_url == expected_url, "URL is not correct"