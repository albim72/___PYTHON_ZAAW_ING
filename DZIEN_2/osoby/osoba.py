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
              f"wzrost: {self.wzrost} cm")

    def wiek_za_n_lat(self, n: int) -> int:
        return self.wiek + n

    def czypracownik(self) -> bool:
        return self.pracownik
