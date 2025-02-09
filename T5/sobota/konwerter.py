# Modul konwertujacy jednostki odleglosci

przelicznik = 0.621371

def km_na_mile(kilometry):
    '''Funkcja przeliczajaca kilometry na mile'''
    return kilometry * przelicznik

def mile_na_km(mile):
    '''Funkcja przeliczajaca mile na kilometry'''
    return mile / przelicznik