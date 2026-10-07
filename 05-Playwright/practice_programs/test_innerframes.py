import pytest

from playwright.sync_api import Page, expect

def test_inner_frame(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    #to locate frame 3:
    frame3 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3")

    frame3.locator("input[name='mytext3']").fill("AKON")

    child_frames = frame3.child_frames
    print("Number of inner frames:", len(child_frames))

    innerframes = child_frames[0]

    radio = innerframes.get_by_label("I am a human")
    radio.check()

    expect(radio).to_be_checked()

    page.wait_for_timeout(3000)

# page.frame()          -> get a frame
# frame.locator()       -> locate inside frame
# child_frames          -> get inner frames
# child_frames[0]       -> first inner frame
# get_by_label()        -> locate using label
# check()               -> select checkbox/radio
# to_be_checked()       -> verify selected
#
# IMPORTANT:
# Once inside a frame, use the FRAME object to locate
# elements inside that frame.
#
# Main flow:
# Page → Frame → Child Frame → Element → Action → Verify
