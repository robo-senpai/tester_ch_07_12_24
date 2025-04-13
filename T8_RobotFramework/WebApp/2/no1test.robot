*** Settings ***
Documentation    1st exmple test using Robot Framework

*** Test Cases ***
Hello World # nazwa testu, może być jakakolwiek, z polskimi znakami itp.
    [Documentation]    Opis testu, np. Test sprawdza, czy 2+2=4
    ${result}=  Evaluate    2+2    # oblicz 2+2 i zapisz wynik w zmiennej
    Should Be Equal As Integers    ${result}   4    # porownaj wynik z result (mozna też As Numbers, ale pewnie bezdie float)