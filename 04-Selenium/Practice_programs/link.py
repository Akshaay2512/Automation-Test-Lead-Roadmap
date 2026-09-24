import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://www.facebook.com/")
driver.maximize_window()

links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))

for i in links:
    print(i.text)
    print("=======")


driver.find_element(By.LINK_TEXT,"Meta Store").click()

time.sleep(5)