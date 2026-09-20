import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.get("https://amazon.com")

driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)


