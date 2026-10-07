import pytest

from playwright.sync_api import Page, expect

def test_alerts(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames = page.frames

    print("No of Frames=", len(frames))

    page.wait_for_timeout(3000)

    # ways to get frames:
    #Way 1 using CSS locator
    #frame1 = page.frame_locator("frame[src='frame_1.html']")

    #way 2 using url
    frame1 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_1")

    #way 3 using name
    #frame1 = page.frame(name="mytext1")

    inputbox = frame1.locator("input[name='mytext1']")
    inputbox.is_enabled()
    inputbox.fill("Akshaay")
    inputbox.is_enabled()

    expect(inputbox).to_have_value("Akshaay")

    page.wait_for_timeout(3000)

# page.frames       -> get all frames
# page.frame()      -> get frame
# frame.locator()   -> locate inside frame
#
# is_enabled()      -> returns True/False immediately
# to_be_enabled()   -> Playwright assertion + auto-wait
#
# fill()            -> enter/replace input value
# to_have_value()   -> verify input value
#
# Input field:
# fill() → to_have_value()
#
# Main flow:
# Page → Frame → Input → Check → Fill → Verify
