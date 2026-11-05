
from playwright.sync_api import Page, expect


def test_login(page: Page):

    # Open login website
    page.goto("https://the-internet.herokuapp.com/login")

    # Enter username
    page.locator("#username").fill("tomsmith")

    # Enter password
    page.locator("#password").fill("SuperSecretPassword!")

    # Click login button
    page.locator('button[type="submit"]').click()

    # Verify successful login
    expect(page.locator("#flash")).to_contain_text(
        "You logged into a secure area!"
    )
