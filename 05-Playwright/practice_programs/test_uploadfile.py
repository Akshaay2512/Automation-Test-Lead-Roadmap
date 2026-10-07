import pytest

from playwright.sync_api import Page, expect

@pytest.mark.skip
def test_singlefile(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    singlefile = page.locator("#singleFileInput").set_input_files(r"D:\Ak Job files\Coverletter.docx")
    page.get_by_role("button",name="Upload Single File").click()

    expect(page.locator("#singleFileStatus")).to_contain_text("Coverletter")

    print("Success!!")

    page.wait_for_timeout(5000)

def test_multiplefile(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    files = [r"D:\Ak Job files\Coverletter.docx",r"D:\Ak Job files\Akshaay Kiran K - [6_9].pdf"]
    page.locator("#multipleFilesInput").set_input_files(files)

    page.get_by_role("button", name="Upload Multiple Files").click()

    message=page.locator("#multipleFilesStatus")
    expect(message).to_contain_text("Coverletter")
    expect(message).to_contain_text("Akshaay Kiran K - [6_9]")

    page.wait_for_timeout(5000)

