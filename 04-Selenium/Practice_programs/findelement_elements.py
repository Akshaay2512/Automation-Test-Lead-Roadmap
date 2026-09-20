#to find all the links available in footer
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.facebook.com/")
driver.maximize_window()

footer = driver.find_element(By.XPATH,"//a[normalize-space()='Sign up']/ancestor::div[.//a[normalize-space()='Log in']][1]")

footer_links = footer.find_elements(By.XPATH, ".//a")


print("Total footer links:", len(footer_links))

for link in footer_links:
    print(link.text)
    print("-------")

print("I want this link:",footer_links[22].text) # to print only the required link text