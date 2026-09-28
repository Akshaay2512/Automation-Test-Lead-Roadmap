import pytest

from playwright.sync_api import Page, expect

'''
logic here is we need to take the actual list and 
also we need to create expected list using sorted method and make that as expected so 
once you compare the actual list and expected list if is equal it is sorted else not sorted
if it is descending order use reverse method after sorting
'''

def test_sorted_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # unsorted_dropdown = page.locator("#colors>option")
    sorted_dropdown = page.locator("#animals>option")
    options = sorted_dropdown.all_text_contents()

    actual = [text.strip() for text in options]
    expected = sorted(actual)

    print("Actual:", actual)
    print("Expected:", expected)


    assert actual == expected, "Dropdown is not sorted" #no option in playwright so using pytest
