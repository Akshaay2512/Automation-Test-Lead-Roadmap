import pytest
from selenium.webdriver.common.by import By


#when TC has multiple scenario combination

@pytest.mark.parametrize("search_item, book_title, book_price", [("python book","Python Crash Course, 3rd Edition: A Hands-On, Project-Based Introduction to Programming", "Paperback\n\nINR 2,369.12"),
                                                                 ("java book", "Java for Beginners: Build Your Dream Tech Career with Engaging Lessons and Projects", "Paperback\n\nINR 1,397.76")])
def test_parameter_demo(launch_browser, search_item, book_title, book_price):
    driver = launch_browser
    driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys(search_item)
    driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
    driver.find_element(By.XPATH,"//h2//span[contains(text(),'"+book_title+"')]").click()
    bookprice = driver.find_element(By.XPATH,"//a[@id='a-autoid-1-announce']").text
    print(bookprice)
    assert bookprice == book_price , "Price not matching"




