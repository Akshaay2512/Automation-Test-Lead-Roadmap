import pytest

from playwright.sync_api import Page, expect

def test_order_dropdown(page: Page):
    page.goto("https://bstackdemo.com/")

    #locating whether dropdown is available and enabled
    order_by = page.locator("Select")  #when you have only value
    expect(order_by).to_be_visible()
    expect(order_by).to_be_enabled()

    #from dropdown select "lowest to highest"
    order_by.select_option("lowestprice")


    page.wait_for_timeout(2000)

    # taking the count of all products:
    products_count = page.locator(".shelf-item")
    print(products_count.count())

    #taking product names:
    products_names = page.locator(".shelf-item__title")

    # print in loop for product names
    for product in products_names.all_text_contents():
        print(product.strip())

    # #Using range function:
    # products = page.locator(".shelf-item__title")
    # for i in range(products.count()):
    #     print(products.nth(i).text_content())

    # taking the product price and print all the price values
    product_price = page.locator(".val")

    for price in product_price.all_text_contents():
        print(price.strip())


    #lowest price:
    print("Lowest price:", products_names.first.text_content().strip(), product_price.first.text_content().strip())


    #Higest price:
    print("Highest:", products_names.last.text_content().strip(), product_price.last.text_content().strip())


    #to click on add to cart of selected product:
    selected_product = page.locator(".shelf-item").filter(has_text="iPhone 12 Pro Max")
    print(selected_product.inner_text())
    print(selected_product.count())

    selected_product.locator("button").click()

    page.wait_for_timeout(3000)
    # selected_product.get_by_role("button", name="Add to cart").click()
    # checkout = page.get_by_role("button", name="Checkout")
    # expect(checkout).to_be_visible()
    # expect(checkout).to_be_enabled()








