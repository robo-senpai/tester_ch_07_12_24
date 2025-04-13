*** Settings ***
Documentation    Test metody post
Library    RequestsLibrary

*** Test Cases ***
Dodanie nowego posta
    [Documentation]    Test wysyła post do API, tworząc nowy wpis i weryfikuje odpowiedź
    ${body}=    Create Dictionary    title    Testowy post    body    To jest treść testowego posta    userId    1
    ${response}=    POST    https://jsonplaceholder.typicode.com/posts    json=${body}
    ${response_body}=    Evaluate    ${response.text}
    Should Be Equal As Integers    ${response.status_code}    201
    Should Be Equal As Integers    ${response_body}[userId]    1
    Should Be Equal    ${response_body}[title]    Testowy post
    Dictionary Should Contain Key    ${response_body}    id
    Should Be True    ${response_body}[id] > 0
    Log    ${response_body}    console=True