miasto = "Lublin"
imie = "Olga"
wiek = 43.5

print("Osoba: " + imie + ", wiek: " + str(wiek))
print(imie,wiek)

dane = "Osoba: {}, wiek: {}, miasto: {}"
print(dane.format(imie,wiek,miasto))

dane = "Osoba: {0}, miasto: {2}, wiek: {1}"
print(dane.format(imie,wiek,miasto))

#f-string
print(f"osoba: {imie}, wiek: {wiek:.2f}, miasto: {miasto}")

owoce = [
    ('awokado',8.99),
    ('malina',13.55),
    ('jabłko',2.33),
    ('mandarynka',8.01),
    ('kiwi',2.67),
    ('winogrono białe',12.44)
]

enowoce = enumerate(owoce)
print(list(enowoce))
print(type(enowoce))

print("__________cennik owoców__________")
for i,(nazwa,cena) in enumerate(owoce):
    print('#%d: %-15s = %6.2f zł' %(i,nazwa,cena))

print("__________cennik owoców II__________")
for i,(nazwa,cena) in enumerate(owoce):
    print('#%d: %-15s = %6.2f zł' %(
        i+1,
        nazwa.title(),
        round(cena,1)
    ))
