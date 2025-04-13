*** Settings ***
Documentation    Test metody DELETE
Library    RequestsLibrary

*** Test Cases ***
Usuniecie istniejacego wpisu
    [Documentation]    Wysyla DELETE, aby usunac post i sprawdza odpowiedz
    ${response}=    DELETE    https://jsonplaceholder.typicode.com/posts/2000
    Should Be Equal As Integers    ${response.status_code}    200
    Should Be Equal    ${response.text}    {}