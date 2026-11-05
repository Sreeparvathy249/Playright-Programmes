
import re
from playwright.sync_api import Page, expect


def test_open_google_website(page: Page):

    # Open Google website
    page.goto("https://www.google.com")

    # Verify page title contains Google
    expect(page).to_have_title(re.compile("Google"))
