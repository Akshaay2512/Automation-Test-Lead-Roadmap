import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://www.html-code-generator.com/drop-down/country-names")
driver.maximize_window()


dropdown1=driver.find_element(By.XPATH,"//select[@id='lang']")
# select = Select(dropdown1)
#
# select.select_by_visible_text("Dutch - Nederlands")
# select.select_by_value("da")
# select.select_by_index(10)

# selected_option = select.first_selected_option
#
# assert selected_option.text == "Dutch - Nederlands"

dropdown1.options


print("Dropdown selection is successful")

time.sleep(5)

driver.quit()




