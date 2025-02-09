from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("#username", "student")
    page.fill("#password", "incorrectPassword")
    page.click("#submit")

    error_message = "Your password is invalid!"

    assert error_message in page.text_content("#error")
    print(f"komunikat to: {error_message}")

    browser.close()