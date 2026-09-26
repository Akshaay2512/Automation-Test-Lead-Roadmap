
from playwright.sync_api import Page, expect

# page.get_by_alt_text()
# page.get_by_text()
# page.get_by_role()

'''when we need to locate images or logo in webpage alt_text() can be used'''


def test_verify_pwlocators(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #timout in playwright
    page.wait_for_timeout(8000) #8000ms is 8secs

    # 1) page.get_by_alt_text()
    logo = page.get_by_alt_text("orangehrm-logo").nth(1)  #.nth(1) at which position the element is available starts from 0
    expect(logo).to_be_visible()

    # 2) page.get_by_text()
    expect(page.get_by_text("Forgot your password? ")).to_be_visible()


    # 3) page.get_by_role() based on w3c standards
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    # 4) page.get_by_label()
    # page.get_by_label("Username").fill("Admin")  #wont work for this website

    # 5) page.get_by_placeholder()
    page.get_by_placeholder("Username").fill("Admin")
    page.wait_for_timeout(3000)


    # 6) get_by_title()
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    page.wait_for_timeout(3000)

    expect(page.get_by_title("Home page link")).to_have_text("Home")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")

    # 7) page.get_by_test_id()
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")

    page.close()



