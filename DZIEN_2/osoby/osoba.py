class Osoba:
    def __init__(self, imie: str, wiek: int, waga: float, wzrost: float):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczu = "brązowe"
        self.pracownik = False
        self.info()

    @staticmethod
    def info() -> None:
        print("nowa osoba została utworzona...")

    def print_osoba(self) -> None:
        print(f"Osoba -> imię: {self.imie}, wiek: {self.wiek}, waga: {self.waga} kg, "
              f"wzrost: {self.wzrost} cm, kolor_oczu: {self.kolor_oczu}")

    def wiek_za_n_lat(self, n: int) -> int:
        return self.wiek + n

    def czypracownik(self) -> bool:
        return self.pracownik

    def zmiana_koloru(self,nowykolor):
        self.kolor_oczu = nowykolor
    
    
    def bmi(self):
        return self.waga/(self.wzrost/100)**2
    
    def opis_bmi(self):
        if self.bmi()<18.5:
            return "niedowaga"
        elif self.bmi()<=25:
            return "waga prawidłowa"
        elif self.bmi()<=30:
            return "nadwaga"
        else:
            return "otyłość"
