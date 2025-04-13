*** Settings ***
Library    MyLib.py

*** Test Cases ***
Test Funkcji Python greet
    ${msg}=    greet    Robotto
    Should Be Equal    ${msg}    Hello, Robotto!
    Log    ${msg}    console=True

Test Funkcji Python add
    ${result}=    add    2    3
    Should Be Equal As Integers    ${result}    5
    Log    Wynik to ${result}    console=True

Python inline sample
    [Documentation]    Test to check Python inline code execution
    ${list}=    Evaluate    [x*x for x in range(5)]
    Log    ${list}    console=True
    ${dict}=    Evaluate    {"a":1, "b":2}
    Log    ${dict}    console=True
    ${random_mod}=    Evaluate    __import__("random").randint(1, 10)
    Log    ${random_mod}    console=True