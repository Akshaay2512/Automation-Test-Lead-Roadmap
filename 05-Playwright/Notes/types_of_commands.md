**In playwright:**

**to be commands:**
expect(locator).to_be_visible()
expect(locator).to_be_enabled()
expect(locator).to_be_disabled()
expect(locator).to_be_checked()
expect(locator).to_be_editable()
expect(locator).to_be_empty()
expect(locator).to_be_focused()
expect(locator).to_be_hidden()

**Example:**
username = page.locator("#username")
expect(username).to_be_visible()
expect(username).to_be_enabled()

**to have commands:**
expect(locator).to_have_text("Login")
expect(locator).to_have_value("Admin")
expect(locator).to_have_attribute("value", "male")
expect(locator).to_have_class("form-control")
expect(locator).to_have_count(3)

**Example:**
username = page.locator("#username")
expect(username).to_have_value("Admin")

**is commands: These don't use expect()**
locator.is_visible()
locator.is_enabled()
locator.is_disabled()
locator.is_checked()
locator.is_editable()
locator.is_hidden()

**Example:**
username = page.locator("#username")
if username.is_visible():
    print("Username is visible")


****One-line revision note****

to_be = state assertion
to_have = value/property assertion
is_ = returns Boolean.