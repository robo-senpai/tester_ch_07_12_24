*** Settings ***
Documentation    Test metody GET z parametrami
Library    RequestsLibrary

*** Test Cases ***
Filtrowanie komentarzy po postID
    [Documentation]    Sprawdza czy GET zwraca tylko komentarze powiazane z postem o id=1
    ${params}=    Create Dictionary    postId=1    # Create a dictionary with query parameters
    Log    ${params}    console=True
    ${response}=    GET    https://jsonplaceholder.typicode.com/comments    params=${params}
    # LUB jako jedna linijka z in-url params
    # ${response}=    GET    url=https://jsonplaceholder.typicode.com/comments?postId=1
    Should Be Equal As Integers    ${response.status_code}    200
    ${comments}=   Evaluate    ${response.text}    # or ${response.json()}
    ${count}=    Get Length    ${comments}    # Get the number of comments (length of the list)
    Should Be Equal As Integers    ${count}    5
    FOR    ${comment}    IN    @{comments}
        Should Be Equal As Integers    ${comment}[postId]    1
    END