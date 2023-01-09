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
