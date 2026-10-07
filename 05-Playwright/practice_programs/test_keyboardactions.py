import pytest

from playwright.sync_api import Page, expect


def test_keyboard(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    input1 = page.locator("#input1")

    # keyboard to be pointed on the text field
    input1.focus()

    # provide text in input box
    page.keyboard.insert_text("Playwright")

    # select the select ctrl+a
    page.keyboard.press("Control+A")

    #copy the text
    page.keyboard.press("Control+C")

    #move the focus to next input box
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    #Paste the text ctrl+v
    page.keyboard.press("Control+V")

    page.wait_for_timeout(5000)

    input2 = page.locator("#input2")
    input3 = page.locator("#input3")

    expect(input2).to_have_value("Playwright")
