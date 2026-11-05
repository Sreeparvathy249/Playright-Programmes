
import pytest
from playwright.sync_api import Page, expect


# Complete Playwright Automation

# 1. Open Google
def test_open_google(page: Page):
    page.goto("https://www.google.com")

    expect(page).to_have_title("Google")


# 2. Open Amazon
def test_open_amazon(page: Page):
    page.goto("https://www.amazon.in")

    expect(page).to_have_title(
        __import__("re").compile("Amazon", __import__("re").IGNORECASE)
    )


# 3. Login Automation
def test_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator('button[type="submit"]').click()

    expect(page.locator("#flash")).to_contain_text(
        "You logged into a secure area!"
    )


# 4. Checkbox Test
def test_checkbox(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkbox = page.locator('input[type="checkbox"]').first
    checkbox.check()

    expect(checkbox).to_be_checked()


# 5. Dropdown Test
def test_dropdown(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")

    dropdown = page.locator("#dropdown")
    dropdown.select_option("1")

    expect(dropdown).to_have_value("1")


# 6. Alert Test
def test_alert(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.once("dialog", lambda dialog: dialog.accept())

    page.get_by_role(
        "button", name="Click for JS Alert"
    ).click()

    expect(page.locator("#result")).to_have_text(
        "You successfully clicked an alert"
    )


# 7. Screenshot Test
def test_screenshot(page: Page):
    page.goto("https://www.google.com")

    page.screenshot(path="google-screenshot.png")


# 8. Textbox Test
def test_textbox(page: Page):
    page.goto("https://www.google.com")

    textbox = page.locator('textarea[name="q"]')
    textbox.fill("Playwright Testing")

    expect(textbox).to_have_value("Playwright Testing")


# 9. Button Click Test
def test_button_click(page: Page):
    page.goto(
        "https://the-internet.herokuapp.com/add_remove_elements/"
    )

    page.get_by_role("button", name="Add Element").click()

    expect(
        page.get_by_role("button", name="Delete")
    ).to_be_visible()


# 10. Page Navigation Test
def test_page_navigation(page: Page):
    page.goto("https://example.com")

    expect(page.locator("h1")).to_have_text("Example Domain")

    page.goto("https://www.google.com")

    expect(page).to_have_title("Google")
