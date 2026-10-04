import pytest

from playwright.sync_api import Page, expect

# @pytest.mark.skip  #in case you user want to skip this test (click on run this test will be skipped
def test_page_table(page:Page):
    page.goto("https://datatables.net/examples/core/basic_init/zero_configuration.html")

    #using one variable for true condition in while loop
    has_more_pages = True

    while has_more_pages:
        rows = page.locator("#example tbody tr").all()
        for row in rows:
            print(row.inner_text())  # all row values printed from first page

        #clicking on next button
        next_page = page.locator("button[aria-label='Next']")

        page.wait_for_timeout(2000)

        # this will extract the class value for the next button
        # also check for the class attribute value when button in disabled state

        if_disabled = next_page.get_attribute("class")

        # using if condition checking class name when it will become disabled
        if "disabled" in if_disabled:
            has_more_pages=False  # this is to break the while loop
        else:
            next_page.click()  # until the next button is disabled page keeps shifting
    print("="*30)

# 🔁 Logic:
#
# Print rows
#     ↓
# Check Next button
#     ↓
# Disabled?
#   ↙       ↘
# YES       NO
#  ↓         ↓
# STOP     CLICK
#            ↓
#       Next page
#            ↓
#          Repeat

def test_filter_table(page:Page):
    page.goto("https://datatables.net/examples/core/basic_init/zero_configuration.html")
    dropdown = page.locator("#dt-length-0")
    dropdown.select_option(label="25")


    rows = page.locator("#example tbody tr")
    print("No of rows printed", rows.count())

    expect(rows).to_have_count(25)


#practice assignment in blaze demo:

# https://blazedemo.com/





