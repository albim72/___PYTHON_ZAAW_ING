import json

osobajson = '{"name":"Jurek","lastname":"Nowak","age":45,"city":"Gliwice"}'
print(osobajson)
print(type(osobajson))

osoba = json.loads(osobajson)
print(osoba)
print(type(osoba))
print(osoba["city"])

samochod = {
    "marka":"Opel",
    "model":"Vectra",
    "rocznik":2008,
    "poj":1.9
}

jsonsam = json.dumps(samochod,indent=4)
print(jsonsam)

with open("sam.json","w",encoding="utf-8") as f:
    f.write(jsonsam)

with open("sam.json","r",encoding="utf-8") as f:
    auto_dict = json.load(f)

print(auto_dict)
print(type(auto_dict))

print("_____________________________________________")

firma = '{"organizacja":"Fundacja BIOTECH","city":"Krosno","country":"Polska"}'

ekstra = {
    "idprojektu":453235436,
    "zakres":"analiza tesktu AI"
}

z = json.loads(firma)
print(z)
z.update(ekstra)
print(z)

firmanew = json.dumps(z)
print(firmanew)

