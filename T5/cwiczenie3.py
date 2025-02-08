# Utwórz własny moduł o nazwie konwerter.py a następnie wykorzystaj go w głównym programie.
# Moduł konwerter powinien zawierać dwie funkcje:
# km_na_mile - zamienia odległość w kilametrów na mile
# mile_na_km - na odwrót
# Następnie napisz główny program/skrypt (np. o nazwie test_konwerter.py) który importuje moduł konwerter i demonstruje działanie obu funkcji

# to jest moj glowny program

import konwerter

km = 10
mil = 10

# Wyswietlenie przekonwertowanych wynikow
print(f"{km} km to {konwerter.km_na_mile(km):.3f} mil.") # zaokraglenie do 3 miejsc po przecinku
print(f"{mil} mil to {konwerter.mile_na_km(mil):.2f} km.") # zaokraglenie do 2 miejsc po przecinku