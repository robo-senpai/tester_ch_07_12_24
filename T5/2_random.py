import random # importujemy modul do losowania liczb

# wylosuj liczbe z zakresu od 1 do 10

losowa = random.randint(1, 10) # random integer
print("Wylosowana liczba z zakresu 1 do 10 to:", losowa)

# wylosuj 5 liczb z zakresu od 1 do 10i zapisz je w liscie

lista_losowych = random.sample(range(1, 11), 5)

print("Lista liczb wylosowanych samplem z zakresu 1 do 10 to:", lista_losowych)

lista_losowych2 = random.choices(range(1, 11), k=5)

print("Lista liczb wylosowanych choicem z zakresu 1 do 10 to:", lista_losowych2)

lista_losowych3 = [random.randint(1, 10) for _ in range(5)]

print("Lista liczb wylosowanych list comprehension z zakresu 1 do 10 to:", lista_losowych3)