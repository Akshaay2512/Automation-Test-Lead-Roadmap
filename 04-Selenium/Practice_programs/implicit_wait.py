from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(10) #seconds #implicit wait

search = driver.find_element(By.NAME,'q')

search.send_keys("python")
search.submit()

input("please enter to proceed")

driver.find_element(By.XPATH,"//h3[text()='Welcome to Python.org']").click()

time.sleep(4)