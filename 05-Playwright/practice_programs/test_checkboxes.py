import pytest
from playwright.sync_api import Page, expect

def test_checkboxes(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #to work with multiple checkboxes use CSS or labels

    #1 check specific checkbox
    # sunday_box= page.get_by_label("Sunday")
    # sunday_box.check()
    # expect(sunday_box).to_be_checked()
    # page.wait_for_timeout(3000)

    #2 to count all the available check boxes:

        #step1 > to maintain all the check box in list format
    days = ['Sunday', 'Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    checkboxes=[]

    # #approach 1:
    # for i in days:
    #     checkbox = page.get_by_label(i)
    #     checkboxes.append(checkbox)
    #     print(checkboxes)

    #approach 2:(shortcut)

    checkboxes = [page.get_by_label(i) for i in days]
    print("Total check box", len(checkboxes))

    #3 select all check boxes at once and assert

    for j in checkboxes:
        j.check()
        expect(j).to_be_checked()

        page.wait_for_timeout(4000)

    #4 uncheck only last few check boxes:

    for k in checkboxes[-3:]:
        k.uncheck()
        expect(k).not_to_be_checked()

        page.wait_for_timeout(2000)

    #5 toggle check boxes:(like some check boxes already selected and some not selected)

    for checkbox in checkboxes:
        if checkbox.is_checked():
            checkbox.uncheck()
            expect(checkbox).not_to_be_checked()
            page.wait_for_timeout(1000)
        else:
            checkbox.check()
            expect(checkbox).to_be_checked()
            page.wait_for_timeout(2000)

    #6 randomly select the check boxes:
    random = [1,4,5]
    for m in random:
        checkboxes[m].check()
        expect(checkboxes[m]).to_be_checked()
        page.wait_for_timeout(2000)

    #7 select check box based on label
    week = "Friday"

    for label in days:
        if label==week:
            check=page.get_by_label(label)
            check.check()
            expect(check).to_be_checked()
    page.wait_for_timeout(2000)









