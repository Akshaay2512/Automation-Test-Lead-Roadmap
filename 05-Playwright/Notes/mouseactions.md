| Test         | Action                | Function used           | Verification      |
| ------------ | --------------------- | ----------------------- | ----------------- |
| Hover        | Hover over menu       | `hover()`               | Submenu appears   |
| Right click  | Right-click element   | `click(button="right")` | Context action    |
| Double click | Double-click button   | `dblclick()`            | `to_have_value()` |
| Drag & Drop  | Drag source to target | `drag_to()`             | `to_have_text()`  |
# ============================================================
# PLAYWRIGHT MOUSE ACTIONS - REVISION NOTES
# ============================================================

# 1. HOVER
#
# hover() -> moves the mouse over an element.
#
# Example:
# pointer = page.locator(".dropbtn")
# pointer.hover()
#
# Useful for opening hover-based menus/dropdowns.


# 2. HOVER OVER A SUB-MENU OPTION
#
# Example:
# select2 = page.locator(".dropdown-content a").nth(1)
# select2.hover()
#
# nth(1) -> selects the 2nd matching element.
# Index starts from 0.


# 3. RIGHT CLICK
#
# click(button="right") -> performs right mouse click.
#
# Example:
# rightclick = page.locator("div[id='mouse-action-box']")
# rightclick.click(button="right")


# 4. DOUBLE CLICK
#
# dblclick() -> performs double mouse click.
#
# Example:
# doubleclick = page.get_by_role("button", name="Copy Text")
# doubleclick.dblclick()
#
# After the action, verify the result.
#
# Example:
# expect(field2).to_have_value("Hello World!")


# 5. DRAG AND DROP
#
# drag_to(target) -> drags one element to another element.
#
# Example:
# source = page.locator("#draggable")
# target = page.locator("#droppable")
# source.drag_to(target)
#
# Verify the result:
# expect(target).to_have_text("Dropped!")


# ============================================================
# QUICK REVISION
# ============================================================
#
# hover()                -> Move mouse over element
# click(button="right")  -> Right click
# dblclick()             -> Double click
# drag_to(target)        -> Drag and drop
#
# nth(0) -> 1st element
# nth(1) -> 2nd element
#
# Mouse action flow:
# Locate → Perform Mouse Action → Verify Result
# ============================================================