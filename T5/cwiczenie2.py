# Napisz program który wylosuje 5 liczb całkowitych z zakresu 1 - 100 i wyświetli je na ekran.ie 
# Wykorzystaj do tego moduł random. Liczby mogą powtarzać. Wykorzystaj do tego pętle. 
# Wynik ma być zapisany w liście

import random

lista_losowych_5 = []

for i in range(5):
    lista_losowych_5.append(random.randint(1, 100))

print("Wylosowane liczby to:", *lista_losowych_5) # gwiazdka rozpakowuje liste

kolejne_losowe_5 = [random.randint(1, 100) for i in range(5)]

print("Inne wylosowane liczby to: ", *kolejne_losowe_5)