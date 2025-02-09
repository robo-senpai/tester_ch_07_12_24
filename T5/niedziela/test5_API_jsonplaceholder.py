from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # utworz kontekst API - inny niz przegladarki
    request_context = p.request.new_context()
    # wysylamy zapytanie GET do API
    response = request_context.get('https://jsonplaceholder.typicode.com/posts/1')
    # sprawdzamy status odpowiedzi
    status = response.status

    print('Status odpowiedzi to:', status)
    assert status == 200

    # body = response.body()
    body = response.json()
    print('Body odpowiedzi to:', body)

    id = body['id'] # spodziewamy sie 1
    userid = body['userId'] # spodziewamy sie 1
    print('ID to:', id)
    print('UserID to:', userid)

    assert id == 1
    assert userid == 1

    title = body['title']
    print('Typ title to string:', isinstance(title,str))

    assert isinstance(title,str)