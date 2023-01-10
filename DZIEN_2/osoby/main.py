from osoba import Osoba
from pracownik import Pracownik
from student import Student

print("____ Osoba 1 _____")
os1 = Osoba("Jan",34,88,176)
os1.zmiana_koloru("niebieskie")
os1.print_osoba()
n_lat = 6
print(f'wiek osoby za {n_lat} lat -> {os1.wiek_za_n_lat(n_lat)} lat')
print(f'czy osoba jest pracownikiem -> {os1.czypracownik()}')

print("____ Osoba 2 _____")
os2 = Osoba("Olga",27,59,171)
os2.print_osoba()
n_lat = 3
print(f'wiek osoby za {n_lat} lat -> {os2.wiek_za_n_lat(n_lat)} lat')
print(f'czy osoba jest pracownikiem -> {os2.czypracownik()}')

print("____ Pracownik 1 _____")
pr1 = Pracownik("Piotr",45,105,174,"ABC Sp zoo","dyrektor",12,11900)
pr1.print_osoba()
pr1.print_pracownik()
n_lat = 3
print(f'wiek osoby za {n_lat} lat -> {pr1.wiek_za_n_lat(n_lat)} lat')
print(f'czy osoba jest pracownikiem -> {pr1.czypracownik()}')


print("____ Student 1 _____")
st1 = Student("Olaf",22,71,176,"F343534","Budowlany","Budowa mostów",5)
st1.print_osoba()
st1.print_student()
n_lat = 3
print(f'wiek osoby za {n_lat} lat -> {st1.wiek_za_n_lat(n_lat)} lat')
print(f'czy osoba jest pracownikiem -> {st1.czypracownik()}')

print("____ Student 2 _____")
st2 = Student("Olga",23,56,170,"GH674875","Ekonomia","Makroekonomia",6,"XYZ","sekretarka",1,2800)
st2.print_osoba()
st2.print_student()
st2.print_pracownik()
n_lat = 3
print(f'wiek osoby za {n_lat} lat -> {st2.wiek_za_n_lat(n_lat)} lat')
print(f'czy osoba jest pracownikiem -> {st2.czypracownik()}')

print("____ Student 3 _____")
st3 = Student("Robert",22,80,180,"II24345","Informatyka","Sieci komputerowe",5,dyscyplina="biegi ultra",lataupr=5,
              best_wynik="102km 19h 32min 4s")
st3.print_osoba()
st3.print_student()
print(st3.infosport())
n_lat = 3
print(f'wiek osoby za {n_lat} lat -> {st3.wiek_za_n_lat(n_lat)} lat')
print(f'czy osoba jest pracownikiem -> {st3.czypracownik()}')
