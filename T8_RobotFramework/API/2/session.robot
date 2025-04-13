*** Settings ***
Documentation    Wykorzystanie create session
Library    RequestsLibrary

*** Test Cases ***
Create Session Example
    [Documentation]    Test create session with RequestsLibrary
    Create Session    jsonplaceholder    https://jsonplaceholder.typicode.com
    ${response}=    GET On Session    jsonplaceholder    /posts/1
    Should Be Equal As Integers    ${response.status_code}    200