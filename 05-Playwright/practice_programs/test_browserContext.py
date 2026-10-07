from playwright.sync_api import Playwright, expect, Page
import pytest

def test_browsercontext(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context=browser.new_context()


    page1=context.new_page()
    page2=context.new_page()

    page1.goto("https://playwright.dev/")
    page1.wait_for_timeout(3000)
    expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")


    page2.goto("https://www.selenium.dev/")
    page2.wait_for_timeout(3000)
    expect(page2).to_have_title("Selenium")


    print("All the pages verified")

    browser.close()

# Browser Context:
# browser.launch()     -> creates browser
# browser.new_context() -> creates isolated browser context
# context.new_page()   -> creates a page/tab
#
# One context can have multiple pages.
#
# Browser
#    ↓
# Context
#    ├── Page 1
#    └── Page 2
#
# expect(page).to_have_title() -> verifies page title
# browser.close() -> closes browser