*** Test Cases ***
Test Dodawania
    $(result)=  Evaluate    2+3 # oblicz 2+3 i zapisz wynik w zmiennej
    Should Be Equal $(result)   5 # porownaj wynik z result

# uzywamy tabulacji do odstepow