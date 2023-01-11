from decimal import Decimal
from akwizytor import Akwizytor

class AkwizytorNaEtacie(Akwizytor):
    """
    akwizytor, który oprócz prowizji od sprzedaży otrzymuje stałą pensję
    """

    def __init__(self, imie, nazwisko, nr_ubezpieczenia, sprzedaz, prowizja, pensja):
        super().__init__(imie, nazwisko, nr_ubezpieczenia, sprzedaz, prowizja)
        self.pensja = pensja
        
    @property
    def pensja(self):
        return self._pensja
    
    @pensja.setter
    def pensja(self,kwota):
        if kwota < Decimal('0.00'):
            raise ValueError('wartość pensji nie może być ujemna')
        self._pensja = kwota

    def zarobek(self):
        return super().zarobek() + self.pensja
    
    def __repr__(self):
        return (f'Akwizytor na etacie {super().__repr__()}\n'
                f'ryczałt: {self.pensja:.2f} zł')
        
    
        
    
    
