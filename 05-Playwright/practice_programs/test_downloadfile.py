import os.path

import pytest

from playwright.sync_api import Page, expect

def test_download(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.locator("#inputText").fill("Akshaay kiran")
    page.locator("#generateTxt").click()


    #event needs to be created
    page.on("download",lambda download : download.save_as("D:/Ak Job files/downloades/ak.txt"))

    page.locator("#txtDownloadLink").click()

    page.wait_for_timeout(4000)

    if os.path.exists("D:/Ak Job files/downloades/ak.txt"):
        print("Yup file downloaded")
    else:
        print("NOT DOWNLOADED")

    page.wait_for_timeout(5000)

# better approach
import os

from playwright.sync_api import Page, expect


def test_downloads1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.locator("#inputText").fill("Akshaay kiran")
    page.locator("#generateTxt").click()

    # Wait for the download event
    with page.expect_download() as download_info:
        page.locator("#txtDownloadLink").click()

    # Get the downloaded file
    download = download_info.value

    # Save the file
    file_path = r"D:\Ak Job files\downloades\ak.txt"
    download.save_as(file_path)

    # Verify file exists
    if os.path.exists(file_path):
        print("Yup file downloaded")
    else:
        print("NOT DOWNLOADED")
