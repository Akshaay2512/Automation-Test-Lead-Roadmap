import pytest

from playwright.sync_api import Page, expect

def test_dynamic_table(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    table = page.locator("table.table tbody")

    rows=table.locator("tr").all()

    cpu=""
    for row in rows:
        browser = row.locator("td").nth(0).inner_text()
        if browser =="Chrome":
            cpu = row.locator("td:has-text('%')").inner_text()
            print("CPU load of Chrome is", cpu)
            break

    expect(page.locator("p.chrome-cpu")).to_contain_text(cpu)