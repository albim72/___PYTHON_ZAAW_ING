from pracownik import Pracownik
from sport import Sport,Ekstra

class Student(Pracownik,Sport,Ekstra):

    def __init__(self, imie: str, wiek: int, waga: float, wzrost: float, idstudenta: str,wydzial: str,
                 kierunek: str, semestr: int,
                 firma: str = None, stanowisko: str = None, latapracy: int = None,
                 wynagrodzenie: float = None, best_wynik=None, lataupr=None, dyscyplina=None):
        Pracownik.__init__(self,imie, wiek, waga, wzrost, firma, stanowisko, latapracy, wynagrodzenie)
        Sport.__init__(self,dyscyplina,lataupr,best_wynik)
        self.idstudenta = idstudenta
        self.wydzial = wydzial
        self.kierunek = kierunek
        self.semestr = semestr


    def print_student(self) -> None:
        print(f'student {self.idstudenta}, kierunek: {self.kierunek}, wydział: {self.wydzial}, '
              f'semestr: {self.semestr}')

    def czypracownik(self) -> bool:
        return self.firma != None




