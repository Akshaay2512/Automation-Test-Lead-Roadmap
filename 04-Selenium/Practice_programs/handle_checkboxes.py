from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.qapractice.com/practice-different-ui-elements?utm_source=chatgpt.com")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, 500);")

time.sleep(3)

# checkbox1 = driver.find_element(By.XPATH,"//input[@name='option1']")
#
# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",checkbox1)
#
# time.sleep(2)
#
# checkbox1.click()
#
# print("Selected:", checkbox1.is_selected())


checkboxall = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'option')]")
print("Total checkboxes:", len(checkboxall))

# for checkbox in checkboxall:
#     if not checkbox.is_selected():
#         checkbox.click()

# print("All checkboxes selected")

for i in checkboxall:
    i.click()

print("All selected")

for i in checkboxall:
    assert i.is_selected(), "Checkbox is not selected"

print("Assertion passed: All checkboxes are selected")