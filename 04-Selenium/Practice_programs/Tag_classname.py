import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://www.facebook.com/")
driver.maximize_window()


#tag & id  = **tagname # value of id**

# driver.find_element(By.CSS_SELECTOR, "input#_R_1h6kqsqppb6amH1_).send_keys("example@gmail.com")

#tag & class = **tagname.value of class**

# tag & attribute = tagname[attribute=value]
driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")

time.sleep(3)

