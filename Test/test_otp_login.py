from playwright.sync_api import Page, expect


def test_otp_login(page: Page):

    # 1. Open OTP login website
    page.goto("https://practice.expandtesting.com/otp-login")

    # 2. Enter email
    page.get_by_label("Email").fill("practice@expandtesting.com")

    # 3. Click Send OTP
    page.get_by_role("button", name="Send OTP").click()

    # 4. Enter OTP
    page.locator("input").last.fill("214365")

    # 5. Click Verify
    page.get_by_role("button", name="Verify").click()

    # 6. Verify successful login
    expect(page.locator("body")).to_contain_text(
        "success"
    )