from itertools import count

import pytest

from playwright.sync_api import Page, expect

def test_order_dropdown(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    products = page.locator(".product-title")

    count = products.count()
    print("Total number of products=",count)



    for text_product in products.all_text_contents():
        print(text_product.strip())
    print("="*20)

    for inner_product in products.all_inner_texts():
        print(inner_product)

    need1 = products.nth(2).inner_text()
    print("This is the needed product:",need1)

    page.get_by_text("Build your own cheap computer").click()


    page.wait_for_timeout(3000)

def test_filpkart_search(page:Page):
    page.goto("https://www.flipkart.com/")
    page.wait_for_timeout(3000)
    page.locator("//span[@class='b3wTlE']").click()

    search = page.locator("//input[@name='q']").nth(0)

    expect(search).to_be_visible()
    expect(search).to_be_enabled()

    search.fill("iphone18")

    page.wait_for_timeout(3000)

    search_options = page.locator("ul>li")
    print(search_options.all_text_contents())

    for option in search_options.all_text_contents():
        print(option.strip())

    search_options.get_by_text("-pro-max cover").click()


    page.wait_for_timeout(4000)

