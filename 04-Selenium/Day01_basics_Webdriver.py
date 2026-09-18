from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(3)

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(2)
try:
    driver.find_element(By.CLASS_NAME, "orangehrm-login-but").click()
except:
    driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
    print("Exception done")

time.sleep(5)

title1 = driver.title
exp_title ="OrangeHRM"

if title1==exp_title:
    print("Pass")
else:
    print("Fail")

time.sleep(3)