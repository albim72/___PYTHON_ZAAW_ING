from pojazd import Pojazd

p = Pojazd()

print(p.silnik("samochód","osobowy","Opel","Vactra","diesel",1.9))
tr,pr = p.trasa("Lublin","Warszawa",177,1.5)
print(f"trasa: {tr}, {pr}")

print(f"spalanie [l/100km]: {p.spal_100(173,19):.2f}")
p.paliwo = 7.81
print(p.paliwo)

print(f'koszt przejazdu: {p.koszt_przejazdu(173,19,p.paliwo)} zł')

print(p.info(2,"przejazd z dodatkową opłata za autostradę 38 zł"))
