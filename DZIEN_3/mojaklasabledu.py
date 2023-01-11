class MojaKlasaBledu(Exception):
    def __init__(self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("wywołano funkcję __str__")
        if self.message:
            return f'{self.__class__.__name__} -> {self.message}'
        else:
            return f'{self.__class__.__name__} -> brak informacji'


try:
    n = int(input('podaj wartość n: '))
    if n >= 100:
        wynik = "właściwa wartość"
    else:
        raise MojaKlasaBledu('wartość n nie osiągnęła pułapu 100')
except MojaKlasaBledu as mb:
    print(mb)
else:
    print(wynik)
finally:
    print("testowanie własnej klasy błędu")
