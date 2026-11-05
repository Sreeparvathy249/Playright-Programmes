
from playwright.sync_api import Page, expect


# Test 1: Verify Page Title
def test_has_title(page: Page):

    page.goto("https://playwright.dev/")

    # Verify that the title contains Playwright
    expect(page).to_have_title("Playwright")


# Test 2: Get Started Link
def test_get_started_link(page: Page):

    page.goto("https://playwright.dev/")

    # Click the Get Started link
    page.get_by_role("link", name="Get started").click()

    # Verify Installation heading is visible
    expect(
        page.get_by_role("heading", name="Installation")
    ).to_be_visible()
