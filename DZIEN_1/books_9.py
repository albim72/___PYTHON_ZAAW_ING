class Book(object):
    #deklarcja stanu -> konstruktor klasy
    # def __new__(cls, *args, **kwargs):
    #     pass

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

    def setcena(self,nowacena):
        self.cena = nowacena

    def getcena(self):
        return self.cena

b1 = Book(45,"Wiedźmin","Andrzej Sapkowski",39)
print(type(b1))
b1.print_book()
print(f'rabat: {b1.rabat():.2f} zł')
print(f'do zapłaty: {b1.cena - b1.rabat():.2f} zł')
print("_________________________________________")
b2 = Book(67,"Hobbit","J.R.R. Tolkien",36)
b2.oprawa = "twarda"
b2.setcena(41)
b2.print_book()
print(f'rabat: {b2.rabat():.2f} zł')
print(f'do zapłaty: {b2.getcena() - b2.rabat():.2f} zł')



