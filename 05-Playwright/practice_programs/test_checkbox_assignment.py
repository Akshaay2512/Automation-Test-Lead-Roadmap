import pytest
from playwright.sync_api import Page,expect

def test_assignment(page:Page):
    page.goto("https://practice-automation.com/form-fields/")

    #select the check box
