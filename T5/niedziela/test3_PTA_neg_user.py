from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("#username", "incorrectUser")
    # wprowadzenie password
    page.fill("#password", "Password123")
    # kliknięcie przycisku
    page.click("#submit")

    error_message = "Your username is invalid!"

    assert error_message in page.text_content("#error")
    print(f"komunikat to: {error_message}")

    browser.close()