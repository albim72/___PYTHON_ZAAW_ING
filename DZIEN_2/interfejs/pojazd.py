from IPojazd import IPojazd
from iopis import IOpis

class Pojazd(IPojazd,IOpis):

    def silnik(self, rodzaj_poj, kategoria, marka, model, rodzaj_silnika, poj):
        return f"Pojazd -> {rodzaj_poj},{kategoria},marka: {marka},rodzaj silnika: {rodzaj_silnika}"

    def trasa(self, start, koniec, odl, czas_przejazdu):
        trasa = f"początek: {start}, koniec: {koniec},"
        przej = f"odległość: {odl} km, czas przejazdu: {czas_przejazdu} h"
        return trasa,przej

    def spal_100(self, odl, litry):
        return litry*100/odl

    def koszt_przejazdu(self, odl, litry, cena_l):
        return self.spal_100(odl,litry)*(odl/100)*cena_l

    def info(self, id, wpis):
        return f'wpis nr {id}: {wpis}'
