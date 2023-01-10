from osoba import Osoba

class Pracownik(Osoba):
    def __init__(self, imie: str, wiek: int, waga: float, wzrost: float,
                 firma:str,stanowisko:str,latapracy:int,wynagrodzenie:float):
        super().__init__(imie, wiek, waga, wzrost)
        self.firma = firma
        self.stanowisko = stanowisko
        self.latapracy = latapracy
        self.wynagrodzenie = wynagrodzenie
        self.pracownik = True
        
    def print_pracownik(self) ->None:
        print(f'pracownik -> firma: {self.firma}, stanowisko: {self.stanowisko}, '
              f'lata pracy: {self.latapracy}, wynagrodzenie: {self.wynagrodzenie}')
