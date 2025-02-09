# Przy wykorzystaniu Playwright wyślij zapytanie GET do https://jsonplaceholder.typicode.com/users/1. 
# Pobierz z niego wartość z pola 'name' (będzie to imię i nazwisko użytkownika).Następnie również w tym samym skrypcie wykorzystaj Playwright, 
# otwórz stronę wyszukiwarki Google i wyszukaj nazwisko użytkownika (tj. wklej name do Google i wyszukaj informacje).


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request_context = p.request.new_context()
    response = request_context.get('https://jsonplaceholder.typicode.com/users/1')

    status = response.status

    print('status odpowiedzi to:', status)
    assert status == 200

    user_page = response.json()
    username = user_page['name']
    print('Imie i nazwisko to:', username)


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.google.com/search')

    # odrzucenie pop up o ciasteczkach
    #page.click("#W0wltc")
    page.click("button:has-text('Odrzuć wszystko')")

    #wpisanie nazwiska do wyszukiwarki
    page.locator("textarea").first.fill(username)

    # wyszukanie poprzez klik lub enter
    #page.click("input[value='Szukaj w Google']")
    page.press("textarea", 'Enter')

    # pojawi sie captcha, bo google ma zabezpieczenia
    page.wait_for_timeout(3000) # mozna popatrzec XD
    
    print('wyszukano')

    browser.close()