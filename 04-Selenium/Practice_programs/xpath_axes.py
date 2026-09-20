import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# Find the WebElement
element = driver.find_element(By.XPATH,"//a[contains(text(),'The Bombay Burmah')]/self::a")

# Get the text separately
print(element.text)

# Scroll the WebElement into the center
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)

time.sleep(4)