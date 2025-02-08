# Napisz klasę Kalkulator, który umie dodawać, odejmować, mnożyć, dzielić, potęgować i pierwiastkować. 
# wybrane funkcje wewnątrz klasy mają zwracać wartość w return a pozostałe jako print

class Kalkulator:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def dodaj(self):
        return self.a + self.b
    
    def odejmij(self):
        return self.a - self.b
    
    def pomnoz(self):
        return self.a * self.b
    
    def podziel(self):
        return self.a / self.b
    
    def poteguj(self):
        return self.a ** self.b
    
    def pierwiastkuj(self):
        return self.a ** (1/self.b)
    
    def wypisz_dzialania(self):
        print(f"Kalkulator wykonuje dzialania na liczbach {self.a} i {self.b}")
        print(f"{self.a} + {self.b} = {self.dodaj()}")
        print(f"{self.a} - {self.b} = {self.odejmij()}")
        print(f"{self.a} * {self.b} = {self.pomnoz()}")
        print(f"{self.a} / {self.b} = {self.podziel()}")
        print(f"{self.a} do potegi {self.b} to {self.poteguj()}")
        print(f"Pierwiastek {self.b} stopnia z {self.a} to {self.pierwiastkuj()}")

# Tworzymy obiekt klasy Kalkulator
a = int(input("Podaj wieksza liczbe: "))
b = int(input("Podaj mniejsza liczbe: "))
kalkulator_1 = Kalkulator(a, b)

# Wywołujemy metody obiektu kalkulator_9_2
kalkulator_1.wypisz_dzialania()