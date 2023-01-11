from collections import namedtuple

Stud = namedtuple('Student',['name','age','id'])

s = Stud('Olga',21,4564676)
print(f"wiek studenta: {s[1]}")
print(f"imię studenta: {s[0]}")
print(f"identyfiator studenta: {getattr(s,'id')}")

d = ['Karol',21,9780650]
print("instancja namedtuple używa listy: ")
print(Stud._make(d))

g = {'name':'Ula','age':22,'id':123243}
print("instancja namedtuple używa słownika: ")
print(Stud(**g))

print(s._replace(age=23))
print(s)
