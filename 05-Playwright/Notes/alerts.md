# ============================================================
# PLAYWRIGHT ALERTS / DIALOGS - REVISION NOTES
# ============================================================

# 1. Playwright handles JavaScript Alert, Confirmation and Prompt
#    using the "dialog" event.

# 2. "dialog" is a Playwright built-in event.
#    The variable name after lambda is user-defined.
#
#    Example:
#    page.once("dialog", lambda box: box.accept())
#
#    Here:
#    dialog -> built-in Playwright event
#    box    -> user-defined variable name
#    accept -> method to click OK


# 3. SIMPLE ALERT
#    Alert normally has only an OK button.
#
#    accept() -> clicks OK
#
#    Example:
#    page.once("dialog", lambda box: box.accept())
#    page.locator("#alertBtn").click()


# 4. CONFIRMATION ALERT
#    Confirmation dialog has OK and Cancel.
#
#    accept()  -> clicks OK
#    dismiss() -> clicks Cancel
#
#    Example:
#    page.once("dialog", lambda box: box.accept())
#    page.locator("#confirmBtn").click()


# 5. PROMPT ALERT
#    Prompt allows us to enter text.
#
#    accept("text") -> enters text and clicks OK
#    dismiss()      -> cancels the prompt
#
#    Example:
#    page.once("dialog", lambda box: box.accept("Akshaay"))
#    page.locator("#promptBtn").click()


# 6. ON vs ONCE
#
#    page.on("dialog", ...)
#    -> Keeps the event listener active.
#
#    page.once("dialog", ...)
#    -> Handles the next dialog only and then removes the listener.
#
#    For separate alert/confirm/prompt actions,
#    once() is safer because old handlers do not interfere.


# 7. GET TEXT FROM PAGE
#
#    inner_text() -> gets the visible text as a Python string.
#
#    Example:
#    text = page.locator("#demo").inner_text()


# 8. VERIFY ALERT RESULT
#
#    to_have_text() -> verifies the expected complete text.
#
#    Example:
#    expect(page.locator("#demo")).to_have_text("You pressed OK!")
#
#    to_contain_text() -> verifies that the element contains
#    the expected text.
#
#    Example:
#    expect(page.locator("#demo")).to_contain_text("Akshaay")


# 9. IMPORTANT
#
#    expect(locator)       -> Locator assertion
#    expect(locator.inner_text()) -> WRONG for to_have_text()
#
#    inner_text() returns a Python string.
#    Keep the Locator when using Playwright's expect().
#
#    Correct:
#    expect(page.locator("#demo")).to_have_text("You pressed OK!")


# ============================================================
# QUICK REVISION
# ============================================================
#
# Alert       -> accept()
# Confirm OK  -> accept()
# Confirm     -> dismiss() for Cancel
# Prompt      -> accept("text")
# Dialog      -> "dialog"
# One-time    -> page.once("dialog", ...)
# Continuous  -> page.on("dialog", ...)
# Get text    -> inner_text()
# Exact text  -> to_have_text()
# Partial text-> to_contain_text()
#
# Main flow:
# Event -> Handle dialog -> Click button -> Verify result
# ============================================================