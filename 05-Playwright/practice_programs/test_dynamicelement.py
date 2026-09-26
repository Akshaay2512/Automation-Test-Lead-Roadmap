from playwright.sync_api import Page, expect

def test_dynamic(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")


    for i in range(5):
        button = page.locator("//button[text()='START' or text()='STOP']")
        button.click()
        page.wait_for_timeout(5000)

#someother ways:
#CSS
# //button[text()='START'] or text()='STOP']
# //button[@name = 'start' or @name='stop']
# //button[contains(@name,'st')] for using both start and stop
# //button[starts-with(@name,'st')]

#Playwright in built locators(difficult)
# import re
#page.get_by_role("button",name=re.compile(r'ST.*'))

