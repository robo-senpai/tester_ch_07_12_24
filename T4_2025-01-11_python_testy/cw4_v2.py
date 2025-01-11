# ĆWICZENIE 4
# Napisz funkcję o nazwie stworz_album(), która buduje słownik opisujący album muzyczny. 
# Funkcja powinna przyjmować nazwę artysty i tytuł albumu, a następnie zwracać słownik zawierający te dwie informacje.
# Użyj funkcji, aby utworzyć trzy słowniki reprezentujące różne albumy. 
# Wydrukuj każdą wartość zwracaną, aby pokazać, że słowniki poprawnie przechowują informacje o albumie.
# Użyj, None aby dodać opcjonalny parametr, stworz_album()który pozwala Ci przechowywać liczbę utworów w albumie.
# Jeśli linia wywoławcza zawiera wartość liczby utworów, dodaj tę wartość do słownika albumu. 
# Wykonaj co najmniej jedno nowe wywołanie funkcji, które zawiera liczbę utworów w albumie.

def stworz_album(nazwa_artysty, tytul_albumu, liczba_utworow=None):
    slownik_albumow = {"Wykonawca": nazwa_artysty, "Album": tytul_albumu}
    if liczba_utworow != None:
        slownik_albumow["Liczba utworow"] = liczba_utworow
    return slownik_albumow

album1 = stworz_album("Linkin Park", "Meteora")
album2 = stworz_album("Marina and the Diamonds", "The Family Jewels", 12)
album3 = stworz_album(tytul_albumu="Master of Puppets", nazwa_artysty="Metallica")
album4 = stworz_album(nazwa_artysty="Apocalyptica", tytul_albumu="Inquisition Symphony", liczba_utworow=10)
print(album1)
print(album2)
print(album3)
print(album4)