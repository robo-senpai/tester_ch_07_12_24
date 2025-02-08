from figury import Kwadrat, Kolo

# Tworzymy obiekt klasy Kwadrat
kwadrat1 = Kwadrat(5)

# Tworzymy obiekt klasy Kolo
kolo1 = Kolo(3)

print(f'Pole kwadratu o boku {kwadrat1.bok} = {kwadrat1.powierzchnia()}')
print(f'Pole kola o promieniu {kolo1.promien} = {kolo1.powierzchnia():.2f}.')