import pytest
from playwright.sync_api import Page, expect

def test_radio(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    radiobtn = page.locator("#male")

    # visibilty and enable or not
    expect(radiobtn).to_be_visible()
    expect(radiobtn).to_be_enabled()

    #to confirm that radio button is not checked
    expect(radiobtn).not_to_be_checked()

    #select the radio button:
    radiobtn.check()

    # to confirm that radio button is checked
    expect(radiobtn).to_be_checked()

    #select the other radio button
    radiobtnfe = page.locator("#female")
    radiobtnfe.check()

    #check whether the first selected radio button is unchecked
    expect(radiobtn).not_to_be_checked()

    # to get the attribute value of that web element
    value = radiobtn.get_attribute("value")
    print("the value of radio button is", value)

    page.wait_for_timeout(3000)



