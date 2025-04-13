*** Settings ***
Documentation    Test API with Robot Framework: 1st API test
Library    RequestsLibrary    # do obsługi HTTP
Library    Collections    # do obsługi kolekcji

*** Test Cases ***
Przykładowy GET na API
    [Documentation]    Test GET na API
    ${response}=    GET    https://jsonplaceholder.typicode.com/posts/1    # GET request to the API
    Should Be Equal As Integers    ${response.status_code}    200    # Check if the status code is 200 (OK)
    #Log    Response Body: ${response.json()}
    #Log    Response Body: ${response.text}

Sprawdzenie zawartości JSON
    [Documentation]    Test GET na API
    ${response}=    GET    https://jsonplaceholder.typicode.com/posts/1    # GET request to the API
    #${body}=    Evaluate    ${response.text}    # Parse the JSON response
    ${body}=    Set Variable    ${response.json()}
    Should Be Equal As Numbers    ${body}[id]    1

Sprawdzenie header
    [Documentation]    Test GET na API
    ${response}=    GET    https://jsonplaceholder.typicode.com/posts/1    # GET request to the API
    ${header}=    Set Variable    ${response.headers}    # Parse the JSON response
    Should Be Equal    ${header}[content-type]    application/json; charset=utf-8
    Should Contain    ${header}[date]    GMT

Partial content
    [Documentation]    Test GET na API
    ${response}=    GET    https://jsonplaceholder.typicode.com/posts/1
    ${body}=    Set Variable    ${response.json()}
    Should Not Be Empty    ${body}

JSON content
    [Documentation]    Test if JSON contains a specific key and its value is not empty
    ${response}=    GET    https://jsonplaceholder.typicode.com/posts/2
    ${body}=    Set Variable    ${response.json()}
    Dictionary Should Contain Key    ${body}    userId   # Check if the key exists
    ${value}=    Get From Dictionary    ${body}    userId   # Get the value of the key
    Should Be True    ${value}    # Check if the value is not empty

    # ${has_key}=    Evaluate    'userId' in ${body}
    # Should Be True    ${has_key}