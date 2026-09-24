from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://demo.automationtesting.in/Frames.html#google_vignette")
driver.maximize_window()


driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

time.sleep(3)

#From main content to outer iframe
outerframe = driver.find_element(By.XPATH,"//div[@class='container iframes-page-container']")
driver.switch_to.frame(outerframe)

#from outer frame to innerframe
innerframe = driver.find_element(By.XPATH,"")