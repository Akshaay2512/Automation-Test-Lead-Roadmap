from logging import exception

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

mywait=WebDriverWait(driver,10, ignored_exceptions=[NoSuchElementException,exception]) #explicit wait declaration

driver.get("https://www.amazon.com")
driver.maximize_window()

search= mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='twotabsearchextbox']")))
search.send_keys("ultra 26")
search.submit()





