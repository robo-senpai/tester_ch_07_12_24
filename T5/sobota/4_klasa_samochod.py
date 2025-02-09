class Samochod:
    # definicja klasy
    def __init__(self, marka, model): # konstruktor
        # self - odwołanie do aktualnego obiektu, representuje nowo tworzona instancje / obiekt tej klasy
        # atrybuty obiektu 
        self.marka = marka
        self.model = model
        self.predkosc = 0 # predkosc poczatkowa to 0km/h
        self.wlaczony_silnik = False # silnik jest wylaczony
        self.kolor = "czerwony"

    def uruchom_silnik(self):
        # metoda klasy
        print("Silnik zostal uruchomiony.")
        self.wlaczony_silnik = True

    def przyspiesz(self, wartosc):
        # zakladamy, ze atrybut predkosc istnieje
        self.predkosc += wartosc

moj_samochod = Samochod("Toyota", "Yaris") # tworzymy obiekt klasy Samochod
moj_samochod_2 = Samochod.__init__(Samochod, 'Toyota', 'Yaris') # zapis równoważny z powyższym

print(moj_samochod.predkosc) # Toyota
moj_samochod.uruchom_silnik()
print(moj_samochod.wlaczony_silnik)
moj_samochod.przyspiesz(30)
print(moj_samochod.predkosc) # 30