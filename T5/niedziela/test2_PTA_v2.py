from playwright.sync_api import sync_playwright

with open("password.txt") as file:
    pass_word = file.read()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # przechodzimy do strony logowania
    page.goto("https://practicetestautomation.com/practice-test-login/")
    # wprowadzenie username (right click, inspect, copy xpath, ale tutaj starczy w ten sposob; # = ID elementu)
    # ID elementu jest unikalne dla kazdego elementu na stronie

    page.fill("#username", "student")
    # wprowadzenie password

    page.fill("#password", pass_word)
    # kliknięcie przycisku
    page.click("#submit")

    current_url = page.url
    print(f"aktualny adres URL to: {current_url}")

    target_page_url = "logged-in-successfully"
    assert target_page_url in current_url

    # sprawdzenie komunikatu 
    success_message = "Logged In Successfully"
    message = page.text_content("h1")
    print(f"komunikat w naglowku to: {success_message}")
    
    # asercja
    assert success_message in message

    # sprawdzenie czy element z tekstem log out jest widoczny na stronie
    locator_logout = page.locator("text=Log out").is_visible()
    assert locator_logout is True
    # wyświetlenie True dla pewnosci
    print(locator_logout)

    browser.close()