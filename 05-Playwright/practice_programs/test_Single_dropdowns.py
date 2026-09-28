import pytest

from playwright.sync_api import Page, expect

def test_single_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")


    #3 ways of selecting option from dropdown:

    #1 By label
    # page.locator("#country").select_option("India") #by label
    # page.locator("#country").select_option(label="India") #this is also by label

    page.wait_for_timeout(3000)

    #2 by value
    page.locator("#country").select_option("germany")
    # page.locator("#country").select_option(value="germany") #this is also by label
    page.wait_for_timeout(4000)

    #3 by index
    page.locator("#country").select_option(index=4)  #by index

    # total number of options:

    dropdown_option=page.locator("#country>option")
    expect(dropdown_option).to_have_count(10)

    options_drop =dropdown_option.all_text_contents()

    #print all countries line by line:

    for option in options_drop:
        print("This are the options",option.strip())

    page.wait_for_timeout(4000)
