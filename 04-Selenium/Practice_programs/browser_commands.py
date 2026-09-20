import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

time.sleep(6)

driver.close() #closes only one tab

driver.quit() #closes whole browser

time.sleep(3)