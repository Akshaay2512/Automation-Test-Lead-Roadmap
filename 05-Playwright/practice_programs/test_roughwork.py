from playwright.sync_api import Page, expect
import pytest

def select_date_range(page, year, month, day):
    while True:
        checkin_month_year