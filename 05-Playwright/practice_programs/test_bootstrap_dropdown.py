import pytest

from playwright.sync_api import Page, expect

# this is something that dropdown options will not be available in DOM
def test_order_dropdown(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name=" Login ").click()

    page.wait_for_timeout(3000)

# to run this specific test:
#py -m pytest -v test_bootstrap_dropdown.py::test_order_dropdown --headed

    # clicking option from global navigation
    page.get_by_text("PIM").click()  # we have a inner text pim so locating with that

    page.wait_for_timeout(3000)

    # locating the dropdown on whole and clicking
    page.locator("form i").nth(2).click()  # so here form is the main tag and i in the tag where dropdown button available

    page.wait_for_timeout(3000)

    '''before doing this need to freeze the 
    browser by debugged mode and find the dropdown options'''

    #locating the options in dropdown
    options = page.locator("div[role='listbox'] span")  #here we have div as main tag and listbox is role where all the options displayed inside child tag span

    # to find the count of options in the dropdown
    count = options.count()
    print("No of dropdowns:",count)

    #assertion to match the count
    expect(options).to_have_count(count)  # assertion for count

    # print  all the options using all text content
    print("All the options in dropdown===>",options.all_text_contents()) #all_text_contents used to print all the values from main dropdown menu(options)

    # to click the particular option
    options.get_by_text("QA Lead", exact=True).click() #since we do not have option tag in the DOM we need to get the value by matching text

    #Also using loop:

    # for i in range(count):
    #     print(options.nth(i).text_content())
    #
    # #select any one option:
    # for j in range(count):
    #     text = options.nth(j).text_content()
    #     if text == "QA Lead":
    #         options.nth(j).click()
    #         break
    page.wait_for_timeout(3000)






