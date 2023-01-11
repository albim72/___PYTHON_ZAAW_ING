from datetime import date

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def ile_od_narodzin(cls,name,year):
        return cls(name,date.today().year - year)

    @staticmethod
    def czydorosly(age):
        return age >= 18

pr1 = Person('Roman',27)
pr2 = Person.ile_od_narodzin('Anna',1981)

print(pr1.age)
print(pr2.age)

print(Person.czydorosly(45))
print(pr1.czydorosly(pr1.age))

pr3 = Person.ile_od_narodzin('Olaf',12)
pr4 = pr1.ile_od_narodzin("Ula",23)

print(pr3 == pr4)

