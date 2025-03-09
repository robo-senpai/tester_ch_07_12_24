import pandas as pd
import numpy as np

data = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
series = pd.Series(data)

# print(series)

series2 = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']) # nadaje swoje indeksy

# print(series2)

# print(series2['a']) # wybieranie po indeksie

macierz = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12],
    'D': [10, 11, 12, 13],
    'E': [10, 11, 12, 13]
}

macierz2 = {
    'A': [1, 2, 3, 4],
    'G': [5, 6, 7, 8],
    'H': [7, 8, 9, 10],
    'I': [20, 21, 22, 23],
}

df = pd.DataFrame(macierz)
df2 = pd.DataFrame(macierz2)

print(df2)
print(df2.T) # transpozycja - zamiana wierszy z kolumnami

print(df2.info()) # informacje o danych
print(df2.describe()) # statystyki opisowe
print(df2.describe().T) # statystyki opisowe transponowane

print(f'liczba wierszy i kolumn:', df2.shape)

print(df2.sort_values(by='I')) # sortowanie po kolumnie I

df2['F'] = [10, 11, np.nan, 13] # dodanie nowej kolumny
print(df2)
print(df2.describe().T)