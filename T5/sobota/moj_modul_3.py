import getpass
username = getpass.getuser()

def przywitaj(imie):
    """Funkcja witajaca z podanym imieniem."""
    print(f"Czesc, {imie}! Milo cie poznac.")

def policz_do_trzech():
    """Funkcja wypisujaca kolejne liczby od 1 do 3."""
    for i in range(3):
        print(i+1)

wiadomosc_powitalna = "Witaj w moim module!"