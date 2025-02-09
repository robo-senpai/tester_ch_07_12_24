#Przy wykorzystaniu Playwright wyślij zapytanie GET do 'https://jsonplaceholder.typicode.com/posts' i sprawdź czy w odpowiedzi znajduję się więcej niż jeden element. 
#Jeśli jest ich więcej niż zero, na konsoli wyświetl ile ich jest'

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # utworz kontekst API - inny niz przegladarki
    request_context = p.request.new_context()
    response = request_context.get('https://jsonplaceholder.typicode.com/posts/')
    body = response.json()

    if body is not None:
        print('Ilosc elementow to:', len(body))
    else:
        print('Brak elementow w odpowiedzi')
    # print('Body odpowiedzi to:', body)