from playwright.sync_api import Page,expect
import pytest

def select_date(page,target_year, target_month, target_date, is_future):
    while True:
        current_month = page.locator(".ui-datepicker-month").text_content().strip()
        current_year =  page.locator(".ui-datepicker-year").text_content().strip()

        print("CURRENT:", current_year,current_month)

        if current_year==target_year and current_month==target_month:
            break
        if is_future==True:
            page.locator(".ui-datepicker-next").click()
        else:
            page.locator(".ui-datepicker-prev").click()

    all_dates = page.locator(".ui-datepicker-calendar td").all()

    for dt in all_dates:
        date_text = dt.inner_text()
        if date_text==target_date:
            dt.click()
            break


def test_jquery_calender(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    calendar1 = page.locator("#datepicker")



    # calendar1 = page.locator("#datepicker").fill("12/12/2012")

#approach 1:
    # expect(calendar1).to_have_value("12/12/2012")
    #
    # page.wait_for_timeout(3000)

#approach 2:
    is_future = True
    year = "2027"
    month = "December"
    date = "25"
    calendar1.click()
    select_date(page,year,month,date, is_future)
    print("Selected date is ===>",calendar1.input_value())

    expect(calendar1).to_have_value("12/25/2027")

    page.wait_for_timeout(5000)

