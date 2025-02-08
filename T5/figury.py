from math import pi

class Kwadrat:
    def __init__(self, bok: int):
        self.bok = bok

    def powierzchnia(self):
        return self.bok ** 2

class Kolo:
    def __init__(self, promien: int):
        self.promien = promien
    
    def powierzchnia(self):
        return pi * (self.promien ** 2)