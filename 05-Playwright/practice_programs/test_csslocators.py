import pytest
from playwright.sync_api import Page, expect


'''
Common combinations:
tag id
tag class
tag attribute
tag class attributes
'''
def test_verify_css(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    # tag id
    # page.locator("input#small-searchterms").fill("Shirts")  #even without tag it will work
    # page.wait_for_timeout(5000)

    #tag and class
    # page.locator("input.search-box-text").fill("pant")
    # page.wait_for_timeout(5000)

    #tag and attribute
    # page.locator("input[name=q]").fill("suits")
    # page.wait_for_timeout(5000)

    #tag, class and attributes
    # page.locator("input.search-box-text[value='Search store']").fill("Trousers")
    # page.wait_for_timeout(5000)