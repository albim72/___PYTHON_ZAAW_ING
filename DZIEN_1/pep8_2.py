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
    ('kiwi',2.67)
]
