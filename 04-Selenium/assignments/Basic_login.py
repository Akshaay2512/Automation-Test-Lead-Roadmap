import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
act_title = driver.title
exp_title="nopCommerce demo store. Logn"

if exp_title==act_title:
    print("ok")
else:
    print("Not ok")


driver.find_element(By.XPATH,"//input[@id='Email']").clear()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH,"//input[@id='Password']").clear()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("admin")

time.sleep(3)

# //tagname[contains(text(), 'substring')]

driver.find_element(By.XPATH,"//button[contains(normalize-space(),'Log in')]").click()

time.sleep(5)