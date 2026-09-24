import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Explicit wait
mywait = WebDriverWait(driver, 10, ignored_exceptions=[NoSuchElementException])

driver.get("https://demoqa.com/alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[@id='promtButton']").click()
time.sleep(2)

alert1 = driver.switch_to.alert #switch to alert
print(alert1.text)
alert1.send_keys("Welcome")

time.sleep(3)

alert1.accept() #to click on ok and close the alert

time.sleep(2)

driver.find_element(By.XPATH,"//button[@id='alertButton']").click()
time.sleep(2)

alert2 = driver.switch_to.alert
print(alert2.text)

time.sleep(2)

alert2.accept()

time.sleep(2)

driver.find_element(By.XPATH, "//button[@id='timerAlertButton']").click()

alert3 = mywait.until(EC.alert_is_present())

print(alert3.text)

alert3.accept()

driver.quit()

#Authentication alert username and password needs to be given in url itself
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# time.sleep(3)
