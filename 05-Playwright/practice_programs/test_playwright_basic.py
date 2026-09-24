from playwright.sync_api import Page, expect


def test_pageurl(page:Page):
    page.goto("https://www.facebook.com") #launch browser and go to given website
    expect(page).to_have_url("https://www.facebook.com/")
    print(page.title())

def test_title(page:Page):
    page.goto("https://www.facebook.com")
    expect(page).to_have_title("Facebook")

def test_capture_url(page:Page):
    page.goto("https://www.facebook.com")
    my_url = page.url
    print("This is my url", my_url)

def test_capture_title(page:Page):
    page.goto("https://www.facebook.com")
    my_title = page.title()
    print("This is my title", my_title)



# command to run py -m pytest test_playwright_basic.py -s -v --headed
# command to run only one test: py -m pytest test_playwright_basic.py -s -v --headed
# to run all the test parallel at a time: py -m pytest test_playwright_basic.py -s -v --headed -n 4
