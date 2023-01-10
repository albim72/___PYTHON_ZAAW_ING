from funkcje.bfunkcje import *

class CDane:
    def __init__(self,lista,slownik):
        self.lista = lista
        self.slownik = slownik

    def czyt_l(self):
        return czytaj_liste(self.lista)

    def czyt_s(self):
        return czytaj_slownik(self.slownik)


