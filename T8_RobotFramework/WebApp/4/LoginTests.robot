*** Settings ***
Documentation    Testy logowania do aplikacji the-internet
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    Chrome
${LOGIN_URL}    https://the-internet.herokuapp.com/login
${VALID_USER}    tomsmith
${VALID_PASS}    SuperSecretPassword!
${INVALID_USER}    invalid_user
${INVALID_PASS}    invalid_password
${FLASH_MESSAGE}    ${EMPTY}

*** Test Cases ***
Udane Logowanie
    [Tags]    positive    login
    [Documentation]    Test udanego logowania z poprawnymi danymi
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Wait Until Element Is Visible    id:username    timeout=5s
    Input Text    id:username    ${VALID_USER}
    Input Password    id:password    ${VALID_PASS}
    Click Button    css:.radius
    Element Should Be Visible    css:a[href="/logout"]
    Close Browser

Nieudane Logowanie: złe hasło
    [Tags]    negative    password    login
    [Documentation]    Test nieudanego logowania z błędnym hasłem
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Wait Until Element Is Visible    id:username    timeout=5s
    Input Text    id:username    ${VALID_USER}
    Input Password    id:password    ${INVALID_PASS}
    Click Button    css:.radius
    Element Should Be Visible    css:.flash.error
    ${error_message}=    Get Text    css:.flash.error
    Log    Błąd logowania: ${error_message}    console=True
    ${current_url}=    Get Location
    Should Be Equal    ${current_url}    ${LOGIN_URL}
    Close Browser

Nieudane Logowanie: zły użytkownik
    [Tags]    negative    username    login
    [Documentation]    Test nieudanego logowania z błędnym użytkownikiem
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Wait Until Element Is Visible    id:username    timeout=5s
    Input Text    id:username    ${INVALID_USER}
    Input Password    id:password    ${VALID_PASS}
    Click Button    css:.radius
    Page Should Contain    Your username is invalid!
    ${error_message}=    Get Text    css:.flash.error
    Log    Błąd logowania: ${error_message}    console=True
    ${current_url}=    Get Location
    Should Be Equal    ${current_url}    ${LOGIN_URL}
    Close Browser

Udane Wylogowanie
    [Tags]    positive    logout
    [Documentation]    Test udanego wylogowania z aplikacji
    Zalogowanie
    Click Link    css:a[href="/logout"]
    Page Should Contain    You logged out of the secure area!
    Page Should Contain Element    css:.radius
    ${FLASH_MESSAGE}=    Get Text    css:.flash.success
    Log    Wiadomość po wylogowaniu: ${FLASH_MESSAGE}    console=True
    Close Browser

*** Keywords ***
Zalogowanie
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    id:username    timeout=5s
    Input Text    id:username    ${VALID_USER}
    Input Password    id:password    ${VALID_PASS}
    Click Button    css:.radius