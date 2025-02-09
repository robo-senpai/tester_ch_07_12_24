from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # utworz kontekst API - inny niz przegladarki
    request_context = p.request.new_context()
    # przygotowanie danych do wyslania
    new_post = {"userId": 9, "title": "title sample", "body": "body sample"}
    print('Wysylamy nowy post: ', new_post)
    # wysylamy zadanie POST do API, aby utworzyc nowy post
    response = request_context.post("https://jsonplaceholder.typicode.com/posts", data=new_post)

    status = response.status

    print('Status odpowiedzi to:', status)

    assert status == 201

    result = response.json()
    print('Body posta to:', result)

    system_id = result['userId']
    post_id = new_post['userId']
    print('System ID to:', system_id, 'a wysłane ID to:', post_id)
    assert system_id == post_id

    system_title = result['title']
    print('System title to:', system_title, 'a wysłany title to:', new_post['title'])
    assert system_title == new_post['title']