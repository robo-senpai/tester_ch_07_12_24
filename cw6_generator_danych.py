from faker import Faker
import random

# inicjalizacja generatora Faker
fake = Faker()

def generuj_dane_testowe(liczba_uzytkownikow):
    dane = []
    for i in range(liczba_uzytkownikow):
        uzytkownik = {
            "imie" : fake.first_name(),
            "email" : fake.email(),
            "wiek" : random.randint(18,60)
        }
        dane.append(uzytkownik)
    return dane

# wygeneruje 10 roznych uzytkownikow
dane_losowe = generuj_dane_testowe(10)

for user in dane_losowe:
    print(user)