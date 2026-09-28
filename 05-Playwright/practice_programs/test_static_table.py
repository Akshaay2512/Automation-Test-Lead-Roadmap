from itertools import count

import pytest

from playwright.sync_api import Page, expect

'''
CONCEPTS COVERED:
Locating a table
count()
nth()
all()
all_inner_texts()
inner_text()
Looping through rows
Accessing specific columns
Using if conditions
Filtering data from a table
Converting str → int
Calculating totals
Playwright expect() assertions
'''

from playwright.sync_api import Page, expect


def test_static_table(page: Page):

    # 🌐 Open the website
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)

    # 📋 Locate the table and check it is visible
    table = page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()

    # 1️⃣ ROWS
    # 🔹 Locate all rows → count them → verify the count
    rows = table.locator("tr")
    row_count = rows.count()
    print("Number of rows:", row_count)

    expect(rows).to_have_count(row_count)

    # 2️⃣ COLUMNS
    # 🔹 Locate all header columns → count them → verify the count
    columns = rows.locator("th")
    column_count = columns.count()
    print("Number of columns:", column_count)

    expect(columns).to_have_count(column_count)

    # 3️⃣ PARTICULAR ROW
    # 🔹 nth(2) = 3rd row because index starts from 0
    # 🔹 locator("td") = get all cells from that row
    random_row = rows.nth(2).locator("td")

    # 🔹 all_inner_texts() = get text from multiple elements as a Python list
    random_row_text = random_row.all_inner_texts()

    print("2nd row items values ======>", random_row_text)

    # 🔹 Verify the cells contain the captured text
    expect(random_row).to_have_text(random_row_text)

    # 🔹 Print each cell separately
    print("2nd row values printing...............")

    for i in random_row_text:
        print(i)

    # 4️⃣ PRINT ALL TABLE DATA
    # 🔹 all() converts the Locator into a Python list of row Locators
    all_rows = rows.all()

    # 🔹 [1:] skips the header row
    for all_data in all_rows[1:]:

        # 🔹 Get all cells from the current row
        all_cols = all_data.locator("td").all_inner_texts()

        print(all_cols)

    # 5️⃣ FIND BOOKS BY A PARTICULAR AUTHOR
    # 🔹 Loop through each data row
    # 🔹 td.nth(0) = Book Name
    # 🔹 td.nth(1) = Author
    # 🔹 td.nth(2) = Subject
    # 🔹 td.nth(3) = Price

    print("Printing book names with author Mukesh")

    for all_data in all_rows[1:]:

        cells = all_data.locator("td")

        author_name = cells.nth(1).inner_text()

        if author_name == "Mukesh":

            book_name = cells.nth(0).inner_text()

            # 🔹 \t gives a tab space
            print(f"{author_name}\t{book_name}")

    # 6️⃣ CALCULATE TOTAL PRICE
    # 🔹 Start total from 0
    total = 0

    for all_data in all_rows[1:]:

        # 🔹 Price is the 4th column → nth(3)
        price = all_data.locator("td").nth(3).inner_text()

        # 🔹 Convert text to integer before adding
        total += int(price)

    print("Total price of all books:", total)
# ==========================================================
# 📌 QUICK REVISION
#
# table.locator("tr")       → get all rows
# rows.count()              → count rows
# rows.nth(2)               → 3rd row (index starts from 0)
# row.locator("td")         → get cells of a row
#
# rows.all()                → convert Locator → Python list
# all_rows[1:]              → skip header row
#
# all_inner_texts()         → text of multiple elements → list
# inner_text()              → text of one element
#
# nth(0) → Book Name
# nth(1) → Author
# nth(2) → Subject
# nth(3) → Price
#
# for row in all_rows[1:]   → loop through data rows
#
# int(price)                → convert price text to number
#
# expect(locator)           → Playwright assertion
# assert                    → Python assertion
# ==========================================================