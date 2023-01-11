from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import AkwizytorNaEtacie

class SuperAkwizytor:

    def __repr__(self):
        return "Jestem szefem więc mam wysoki ryczałt"

    def zarobek(self):
        return Decimal('1_000_000.00')

k = SuperAkwizytor()
s = AkwizytorNaEtacie('Olga','Kot','4353454545',Decimal('345000'),Decimal('4'),Decimal('4500'))
c = Akwizytor('Janek','Nowak','75646546',Decimal('556900.0'),Decimal('5.5'))

pracownicy = [c,s,k]

for p in pracownicy:
    print(p)
    print(f'zarobek: {p.zarobek():,.2f}\n')
