# Modul konwertujacy jednostki odleglosci

przelicznik = 0.621371

def km_na_mile(kilometry):
    '''Funkcja przeliczajaca kilometry na mile'''
    return (round((kilometry * przelicznik),2))

def mile_na_km(mile):
    '''Funkcja przeliczajaca mile na kilometry'''
    return (round((mile / przelicznik),2))