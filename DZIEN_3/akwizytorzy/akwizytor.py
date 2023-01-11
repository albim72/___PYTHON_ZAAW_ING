from decimal import Decimal

class Akwizytor:
    """
    Pracownik, którego wynagrodzenie jest wyłącznie prowizją od sprzedaży
    """
    def __init__(self,imie,nazwisko,nr_ubezpieczenia,sprzedaz,prowizja):
        self._imie = imie
        self._nazwisko = nazwisko
        self._nr_ubezpieczenia = nr_ubezpieczenia
        self.sprzedaz = sprzedaz
        self.prowizja = prowizja
        
    @property
    def imie(self):
        return self._imie
    
    @imie.setter
    def imie(self,imie):
        self._imie = imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, nazwisko):
        self._nazwisko = nazwisko

    @property
    def nr_ubezpieczenia(self):
        return self._nr_ubezpieczenia

    @nr_ubezpieczenia.setter
    def nr_ubezpieczenia(self, nr_ubezpieczenia):
        self._nr_ubezpieczenia = nr_ubezpieczenia

    @property
    def sprzedaz(self):
        return self._sprzedaz
    
    @sprzedaz.setter
    def sprzedaz(self,kwota):
        if kwota<Decimal('0.00'):
            raise ValueError('wartość sprzedaży nie może być ujemna')
        self._sprzedaz = kwota

    @property
    def prowizja(self):
        return self._prowizja

    @prowizja.setter
    def prowizja(self, procent):
        if not (Decimal('0.0') <= procent <= Decimal('20.00')):
            raise ValueError('prowizja nie może być ujemna ani większa niż 20%')
        self._prowizja = procent
        
        
        
        
