class Book(object):
    #deklarcja stanu -> konstruktor klasy
    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    #zachowanie -> funkcje klasy(metody)
    def create_book(self):
        print("utworzono nową książkę...")
        

    def print_book(self):
        print(f'ksiązka({self.idbook}) -> tytul: {self.tytul}, autor: {self.autor},'
              f'oprawa: {self.oprawa}, cena: {self.cena} zł')

    def rabat(self):
        return 0.1*self.cena





