class Samochod:
    def __init__(self,marka,model,rocznik,cena,rata):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.cena = cena
        self.rata = rata


    @staticmethod
    def salon(miasto):
        return f'salon sprzedaży, miasto -> {miasto}'

    @classmethod
    def obliczenie_raty(cls,cena,miesiac):
        return cls("Opel","Insignia",2020,156000,1.3*cena/miesiac)

sm = Samochod("Opel","Insignia",2020,156000,1324)
print(sm.salon("Toruń"))
print(sm.rata)

smc = Samochod.obliczenie_raty(178900,52)
print(smc.salon("Radom"))
print(smc.rata)

