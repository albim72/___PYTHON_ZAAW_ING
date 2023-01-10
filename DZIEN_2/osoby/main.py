from osoba import Osoba

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
