*** Settings ***
Documentation    Test metody GET > zadanie > Napisz test, który pobierze dane użytkownika (/users/) i zweryfikuje poprawność danych.
Library    RequestsLibrary

*** Test Cases ***
Weryfikacja danych uzytkownika nr 5
    [Documentation]    Test GET, aby pobrać dane użytkownika i zweryfikować odpowiedź
    ${response}=    GET    https://jsonplaceholder.typicode.com/users/5
    ${user}=    Set Variable    ${response.json()}
    Should Be Equal As Integers    ${user}[id]    5
    Should Be Equal    ${user}[username]    Kamren
    Should Be Equal    ${user}[address][zipcode]    33263
    #${user_str}=    Convert To String    ${user}
    ${user_str}=    Evaluate    str(${user})
    Should Contain    ${user_str}    Kamren
