#import dane
#import dane as dn
from dane import nr_filii as filia
from dane import book as ksiazka
from funkcje.bfunkcje import czytaj_liste,czytaj_slownik
from klasy.kol_klasy import CDane

print(filia)
print(ksiazka)

print("_______________ czytanie kolekcji z użyciem funkcji _____________")
czytaj_liste(filia)
czytaj_slownik(ksiazka)

print("_______________ czytanie kolekcji z użyciem metod obiektu _____________")
cd = CDane(filia,ksiazka)
cd.czyt_l()
cd.czyt_s()
