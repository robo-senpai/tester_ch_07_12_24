import math # importujemy wbudowany modul math

liczba = 16

wynik = math.sqrt(liczba) # pierwiastek kwadratowy z liczby

print(f"Pierwiastek kwadratowy z {liczba} to {wynik}.") # 4.0

promien = 5
pole = math.pi * math.pow(promien, 2) # pole kola

print(f"Pole kola o promieniu {promien} to {int(pole)}.") # 78.53981633974483

pole2 = 80
promien2 = math.sqrt(pole2 / math.pi) # promien kola

print(f"Promien kola o polu {pole2} to {round(promien2,2)}.") # 5.641895835477563
