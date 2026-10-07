from playwright.sync_api import Page,expect
import pytest


def select_date(page, target_year, target_month):

    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    target_month_number = months[target_month]

    while True:

        # Get currently displayed month and year
        current_month = page.locator(".ui-datepicker-month").inner_text().strip()
        current_year = int(page.locator(".ui-datepicker-year").inner_text().strip())

        current_month_number = months[current_month]

        print("CURRENT:", current_year, current_month)

        # Target reached
        if current_year == int(target_year) and current_month == target_month:
            break

        # Target is after current date
        if (current_year, current_month_number) < (int(target_year), target_month_number):
            page.locator(".ui-datepicker-next").click()

        # Target is before current date
        else:
            page.locator(".ui-datepicker-prev").click()

def test_jquery_calender(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    calendar1 = page.locator("#datepicker")

    year = "2027"
    month = "December"

    calendar1.click()

    select_date(page, year, month)

    print("Calendar reached:", year, month)

    page.wait_for_timeout(3000)