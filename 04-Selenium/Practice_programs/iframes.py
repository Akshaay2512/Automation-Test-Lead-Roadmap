from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://practice-automation.com/iframes/")
driver.maximize_window()

driver.switch_to.frame("iframe-1")
driver.find_element(By.XPATH,"//a[contains(text(),'Docs')]").click()

time.sleep(3)
