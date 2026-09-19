import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Create new account").click()

time.sleep(5)

firstname = driver.find_element(By.XPATH,"//input[@id='_R_1cl2p4jikacppb6amH1_']")
firstname.send_keys("Akshaay")

lastname = driver.find_element(By.XPATH,"//input[@id='_R_1kl2p4jikacppb6amH1_']")
lastname.send_keys("Kiran")

time.sleep(2)

# Click Day dropdown
driver.find_element(By.XPATH,"//*[normalize-space()='Day']").click()


time.sleep(1)



print("Number of options:", len(dates))

time.sleep(2)

# Month dropdown
driver.find_element(
    By.XPATH,"//*[normalize-space()='Month']").click()

time.sleep(1)