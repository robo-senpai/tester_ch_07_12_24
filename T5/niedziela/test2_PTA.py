from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # przechodzimy do strony logowania
    page.goto("https://practicetestautomation.com/practice-test-login/")
    # wprowadzenie username (right click, inspect, copy xpath, ale tutaj starczy w ten sposob; # = ID elementu)
    # ID elementu jest unikalne dla kazdego elementu na stronie
    page.fill("#username", "student")
    # wprowadzenie password
    page.fill("#password", "Password123")
    # kliknięcie przycisku
    page.click("#submit")
    # czekamy na przekierowanie do strony zalogowanego uzytkownika
    page.wait_for_url("**/logged-in-successfully/")

    # sprawdzenie komunikatu T5/niedziela/test2_PTA.pyc
    success_message = "Logged In Successfully"
    message = page.text_content("h1")
    print(f"komunikat to: {success_message}")
    
    # asercja
    assert success_message in message

    # sprawdzenie czy element z tekstem log out jest widoczny na stronie
    locator_logout = page.locator("text=Log out").is_visible()
    assert locator_logout is True
    print(locator_logout)

    browser.close()