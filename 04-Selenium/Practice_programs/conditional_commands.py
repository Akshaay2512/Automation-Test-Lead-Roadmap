#is_displayed
#is_enabled
#is_Selected

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

# input("Complete the 'Verify you are human' step, then press Enter...")

time.sleep(3)

address = driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']")
print("Display status:",address.is_displayed())
print("Enabled status:", address.is_enabled())
address.click()
print("Selected status:",address.is_selected())

gender = driver.find_element(By.XPATH,"//input[@value='Male']")
gender.click()

print("Selected status:",gender.is_selected())

driver.quit()