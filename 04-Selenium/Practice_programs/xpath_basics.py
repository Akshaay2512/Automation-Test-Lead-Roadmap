import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://www.amazon.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("iphone18")
time.sleep(3)


suggestions = driver.find_elements(By.XPATH,"//div[@id='sac-autocomplete-results-container']//div[@role='row']")
print("Total suggestions:", len(suggestions))

for suggestion in suggestions:
    print(suggestion.text)
    print("================")

time.sleep(5)

driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()

time.sleep(5)

results =  driver.find_elements(By.XPATH,"//div[@data-component-type='s-search-result']")

print("Total results:", len(results))

for result in results:

    print(result.text)
    print("-------------------------")

    product_name = "Apple iPhone 17 Pro, US Version, 512GB, eSIM, Cosmic Orange- Unlocked (Renewed)"

    if product_name in result.text:
        print("Item available")
        break #remove this if you want to print all the search results

else:
    print("Product not found")

time.sleep(5)

driver.quit()
