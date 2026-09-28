import pytest

from playwright.sync_api import Page, expect

def test_multiple_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #multiple selection by label
    page.locator("#colors").select_option(label=["Red", "Blue", "Green", "Yellow", "Red", "White", "Green"])

    #by index
    page.locator("#colors").select_option(index=[1,2])

    #count number of options
    dropdown_count=page.locator("#colors>option")
    expect(dropdown_count).to_have_count(7)

    #to print all the options from dropdown
    options = dropdown_count.all_text_contents()

    for option in options:
        print(option.strip())



    page.wait_for_timeout(3000)