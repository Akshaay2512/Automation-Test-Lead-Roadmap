import pytest

from playwright.sync_api import Page, expect

@pytest.mark.skip
def test_inner_frame(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    pointer=page.locator(".dropbtn")
    pointer.hover()

    select2 = page.locator(".dropdown-content a").nth(1)
    select2.hover()

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_rightclick(page:Page):
    page.goto("https://techbeamers.com/selenium-practice-test-page/")

    rightclick = page.locator("div[id='mouse-action-box']")
    rightclick.click(button="right")

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_double_click(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    doubleclick = page.get_by_role("button", name="Copy Text")
    doubleclick.dblclick()

    field2 = page.locator("input[id='field2']")

    expect(field2).to_have_value("Hello World!")

    page.wait_for_timeout(5000)

def test_dragdrop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    source = page.locator("#draggable")
    target = page.locator("#droppable")

    source.drag_to(target)

    expect(target).to_have_text("Dropped!")

    page.wait_for_timeout(5000)