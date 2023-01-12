from dataclasses import dataclass

class Liczba:
    def __init__(self,x):
        self.x = x

zkobj = Liczba(2)
print(zkobj.x)

#dataclass
@dataclass
class DLiczba:
    x:int

dkobj = DLiczba(4.8)
print(dkobj.x)

@dataclass
class Dane:
    nazwa:str
    licznik:int = 0
    cena:float = 0.0

prod = Dane("pudełko nr 5",6,11.2)
print(f'{prod.nazwa} -> {prod.cena} zł -> {prod.licznik} sztuk')
