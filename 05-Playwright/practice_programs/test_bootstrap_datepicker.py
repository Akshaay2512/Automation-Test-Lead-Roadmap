from playwright.sync_api import Page,expect
import pytest
from datetime import datetime


def select_checkin_date(page, year, month, day):
    while True:
        checkin_month_year = page.locator("h3[id^='bui-calendar-month-']").nth(0).inner_text()
        current_month, current_year = checkin_month_year.split(" ")

        if current_month==month and current_year==year:
            break
        else:
            next_month = page.get_by_role("button", name="Next month").click()
    all_dates = page.locator("table.b8fcb0c66a tbody").nth(0).locator('td').all()

    for date in all_dates:
        if date.inner_text()==day:
            date.click()
            break

def select_checkout_date(page, year, month, day):
    while True:
        checkout_month_year = page.locator("h3[id^='bui-calendar-month-']").nth(0).inner_text() #if check out date is in next month change nth(0) to nth(1)
        current_month, current_year = checkout_month_year.split(" ")

        if current_month==month and current_year==year:
            break
        else:
            next_month = page.get_by_role("button", name="Next month").click()
    all_dates = page.locator("table.b8fcb0c66a tbody").nth(0).locator('td').all() #if check out date is in next month change nth(0) to nth(1)

    for date in all_dates:
        if date.inner_text()==day:
            date.click()
            break

def test_booking_website(page:Page):
    page.goto("https://www.booking.com/")
    page.wait_for_timeout(3000)

    close_button = page.get_by_role("button", name="Dismiss")

    if close_button.is_visible():
        close_button.click()


    page.get_by_test_id("searchbox-dates-container").click()

    select_checkin_date(page,"2026", "October", "15")
    select_checkout_date(page, "2026", "October", "18")

    checkin_date = page.locator("span[data-testid='date-display-field-start']").inner_text().strip()
    checkout_date = page.locator("span[data-testid='date-display-field-end']").inner_text().strip()

    print("Check in:", checkin_date)
    print("Check out:",checkout_date)

    checkin = datetime.strptime(checkin_date, "%a, %b %d")
    checkout = datetime.strptime(checkout_date, "%a, %b %d")

    #Calculate number of nights
    stay = checkout - checkin

    print("Number of nights:", stay.days)

    #Verify the calculation
    assert stay.days == 3

    page.wait_for_timeout(5000)


# practice #dummyticket.com