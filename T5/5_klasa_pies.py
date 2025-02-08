class Pies:
    '''Klasa reprezentująca psa'''
    def __init__(self, imie, wiek):
        self.name = imie
        self.age = wiek

    def szczekaj(self):
        '''Pies szczeka'''
        print(f'{self.name} szczeka: Hau! Hau!')
        # metoda bez return zwraca None

    def przelicz_wiek(self):
        '''Przelicza wiek psa na ludzki'''
        return self.age * 7

pies_1 = Pies('Reksio', 5)

pies_1.szczekaj() # oczekujemy: Reksio szczeka: Hau! Hau!
print(f'{pies_1.name} ma {pies_1.przelicz_wiek()} ludzkich lat.') # oczekujemy: Reksio ma 35 lat.

print(pies_1.szczekaj())