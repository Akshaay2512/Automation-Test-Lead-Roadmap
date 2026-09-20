import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://www.amazon.com/")
driver.maximize_window()

search = driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
search.send_keys("ultra 26")
print(search.get_attribute('value'))
print("this is text:",search.text)