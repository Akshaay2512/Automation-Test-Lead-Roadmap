import pytest
from playwright.sync_api import Page, expect

def test_input_box(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    textbox=page.locator("#name")

    #visibilty and enable or not
    expect(textbox).to_be_visible()
    expect(textbox).to_be_enabled()

    #check attribute of element
    expect(textbox).to_have_attribute("maxlength","15")

    #to get an attribute value of element
    maxlength = textbox.get_attribute("maxlength")
    print("maximum length:", maxlength)

    #to fill value in the text box
    textbox.fill("Akshaay")

    #to get the entered value:
    enteredvalue = textbox.input_value()
    print("Value in the textbox is:", enteredvalue)

    page.wait_for_timeout(5000)



