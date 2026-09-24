import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_login():
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

#Approach 1:
    # heading = wait.until(EC.visibility_of_element_located((By.XPATH,"//h6[text()='Dashboard']")))
    # if "Dashboard" == heading.text:
    #     print("We are correct")
    #
    # else:
    #     print("NOT TODAY")
    #     raise Exception("Not in dashboard")

# Approach 2:
    try:
        heading = wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

        assert heading.text == "Dashboard", "WE ARE IN DASHBOARD"


    except Exception as k:
        print("NOT TODAY")
        raise

    current_url = driver.current_url.lower()
    if "dashboard" in current_url:
        print("Yes again")
    else:
        print("No")



def test_login_invalid():
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("AK")
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("AKKK1223")
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    invalid = wait.until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Invalid credentials']"))).is_displayed()
    assert True == invalid, "Not matched"

