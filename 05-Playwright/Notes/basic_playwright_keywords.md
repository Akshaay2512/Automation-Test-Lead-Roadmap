READ                  CHECK
 ↓                      ↓
inner_text()       to_have_text()
text_content()     to_have_value() → INPUT

⭐ The easiest way to remember
| Function          | Simple meaning           |
| ----------------- | ------------------------ |
| `inner_text()`    | **READ visible text**    |
| `text_content()`  | **READ element text**    |
| `to_have_text()`  | **CHECK displayed text** |
| `to_have_value()` | **CHECK input value**    |

**Build in locators**
1. get_by_role()
2. get_by_label()
3. get_by_placeholder()
4. get_by_text()
5. get_by_alt_text()
6. get_by_title()
7. get_by_test_id()
8. locator()       ← CSS / XPath when needed

⭐ Most Important Cheat Sheet

**LOCATE**
locator()
get_by_role()
get_by_label()
get_by_test_id()

**STATE**
to_be_visible()
to_be_enabled()
to_be_checked()

**CONTENT**
to_have_text()
to_contain_text()
to_have_value()
to_have_attribute()
to_have_count()

**READ**
inner_text()
text_content()

**BOOLEAN**
is_visible()
is_enabled()
is_checked()

**ACTION**
click()
dblclick()
hover()
fill()
check()
drag_to()

**KEYBOARD**
keyboard.press()

**DIALOG**
page.once("dialog")
accept()
dismiss()

**FRAME**
page.frame()
frame.locator()
child_frames

**COLLECTION**
count()
first
last
nth()
all()
all_text_contents()

| Playwright locator     | When to use                                       | Common elements                                       | Example                                     |
| ---------------------- | ------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------- |
| `get_by_role()`        | When element has a clear **accessible role/name** | Button, link, textbox, checkbox, radio, heading, etc. | `page.get_by_role("button", name="Login")`  |
| `get_by_label()`       | When an element has a **label** connected to it   | Input, checkbox, radio                                | `page.get_by_label("Username")`             |
| `get_by_placeholder()` | When input has a **placeholder**                  | Input, textarea                                       | `page.get_by_placeholder("Enter username")` |
| `get_by_text()`        | When you know the **visible text**                | `<p>`, `<div>`, `<span>`, button, link, etc.          | `page.get_by_text("Welcome")`               |
| `get_by_alt_text()`    | When image has an **alt attribute**               | Images, image links                                   | `page.get_by_alt_text("Profile picture")`   |
| `get_by_title()`       | When element has a **title attribute**            | Button, link, icon, etc.                              | `page.get_by_title("Close")`                |
| `get_by_test_id()`     | When application provides a **data-testid**       | Any element                                           | `page.get_by_test_id("login-button")`       |

⭐ The easiest way to choose
BUTTON with name "Login"
        ↓
get_by_role()

INPUT with label "Username"
        ↓
get_by_label()

INPUT with placeholder "Enter username"
        ↓
get_by_placeholder()

VISIBLE text "Welcome"
        ↓
get_by_text()

IMAGE with alt="Logo"
        ↓
get_by_alt_text()

ELEMENT with title="Close"
        ↓
get_by_title()

ELEMENT with data-testid="login"
        ↓
get_by_test_id()

**get_by_role() is not only for buttons**
page.get_by_role("button", name="Login")
page.get_by_role("link", name="Register")
page.get_by_role("textbox", name="Username")
page.get_by_role("checkbox", name="Remember me")
page.get_by_role("radio", name="Male")
page.get_by_role("heading", name="Welcome")