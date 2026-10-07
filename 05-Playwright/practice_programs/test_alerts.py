import pytest

from playwright.sync_api import Page, expect

def test_alerts(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

# Syntax for lambda : var = lambda parameters : expression
# example:
# x= lambda a,b,c : a+b+c
#print(x(10,20,30))

# Simple alert:
    page.once("dialog", lambda box:box.accept()) # dialog is prebuilt event in JS and box is user defined variable name

    page.locator("#alertBtn").click()

    page.wait_for_timeout(5000)

# Confirmation alert

    page.once("dialog", lambda  box1:box1.accept())

    page.locator("#confirmBtn").click()

    #Approach 1:
    # expect(page.get_by_text("You pressed OK!")).to_have_text("You pressed OK!")

                            #or
    # Approach 2:
    text = page.locator("#demo").inner_text()
    print("The output text is :", text)

    expect(page.locator("#demo")).to_have_text("You pressed OK!")

    page.wait_for_timeout(5000)

#Prompt alert:
    page.once("dialog", lambda box2:box2.accept("Akshaay"))

    page.locator("#promptBtn").click()

    text1 = page.locator("#demo").inner_text()
    print("The name given is", text1)

    expect(page.locator("#demo")).to_contain_text("Akshaay")

