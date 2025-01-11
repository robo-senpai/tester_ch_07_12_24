def pozdrowienia(name1, name2):
    """
    Wyswietlamy proste pozdrowienie
    czy cos
    """
    # jednolinijkowy komentarz tak tez mozna

    print("Hello", name2)
    print(f"Hello {name1} {name2}")
    print("Hello {}".format(name2))
    print("Hello, %s!" % name2) # %s = substitute w/ variable

# pozdrowienia(name1="Earth", name2="World")


# Cwiczenie 1
# Napisz funkcję o nazwie ulubiona_ksiazka(), która akceptuje jeden parametr - tytul. 
# Funkcja powinna wydrukować wiadomość, taką jak Moja ulubiona ksiazka jest Hobbit . 
# Wywołaj funkcję, upewniając się, że tytuł książki jest podany jako argument w wywołaniu funkcji.

def ulubiona_ksiazka(tytul):
    print(f"Moja ulubiona ksiazka to {tytul}")

ulubiona_ksiazka(tytul="1984")

# Cwiczenie 2
# Napisz funkcję o nazwie koszulka(), która akceptuje rozmiar i tekst wiadomości, która powinna zostać wydrukowana na koszulce. 
# Funkcja powinna wydrukować zdanie podsumowujące rozmiar koszulki i wydrukowaną na niej wiadomość.
# Wywołaj funkcję raz, używając argumentów pozycyjnych, aby utworzyć koszulkę. 
# Wywołaj funkcję drugi raz, używając argumentów słów kluczowych.

def koszulka(rozmiar, tekst):
    print(f"Koszulka w rozmiarze {rozmiar} z napisem: {tekst}")

koszulka("M", "Hello World") # argumenty pozycyjne
koszulka(tekst="Hello World", rozmiar="M") # argumenty słów kluczowych

# Cwiczenie 3
# Napisz funkcję miasta_panstwa(), która akceptuje nazwę miasta i jego kraju.
# Funkcja powinna wydrukować proste zdanie, takie jak "Warszawa jest kraju Polska".
# Podaj parametrowi kraju wartość domyślną. Wywołaj swoją funkcję dla trzech różnych miast, 
# z których przynajmniej jedno nie znajduje się w domyślnym kraju.

def miasta_panstwa(miasto, panstwo="Polska"):
    print(f"{miasto} jest w kraju {panstwo}")

miasta_panstwa("Warszawa")
miasta_panstwa("Krakow")
miasta_panstwa("Berlin", "Niemcy")

def miastapanstwa(miasto, ludnosc=0, panstwo="Polska"):
    if ludnosc == 0:
        ludnosc = "NaN"

    miasto_panstwo_slownik = {"panstwo": panstwo, "miasto": miasto, "ludnosc": ludnosc}
    return miasto_panstwo_slownik

miasto_funkcja = miastapanstwa("Paryz", 5000000, "Francja")
miasto_funkcja2 = miastapanstwa("Sandomierz")
print(miasto_funkcja)
print(miasto_funkcja2)
