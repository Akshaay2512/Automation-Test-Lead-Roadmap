#get(url)
#get_title
#get_url
#get_pagesource

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

page_title = driver.title
print(page_title)
actual_title = "OrangeHRM"
org_url = driver.current_url
print(org_url)

if actual_title == page_title:
    print("ALL OK")
else:
    print("fail")

print(driver.page_source)