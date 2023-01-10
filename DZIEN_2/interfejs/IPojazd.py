from abc import ABCMeta, abstractmethod

class IPojazd(metaclass=ABCMeta):

    @property
    def paliwo(self):
        return self._cena_l
    
    @paliwo.setter
    def paliwo(self,cena_l):
        self._cena_l = cena_l
        
    @abstractmethod
    def silnik(self,rodzaj_poj,kategoria,marka,model,rodzaj_silnika,poj):
        raise NotImplementedError(f"obowiązkowo zaimplementuj metodę silnik")
    
    @abstractmethod
    def trasa(self,start,koniec,odl,czas_przejazdu):
        raise NotImplementedError(f"obowiązkowo zaimplementuj metodę trasa")
    
    @abstractmethod
    def spal_100(self,odl,litry):
        raise NotImplementedError(f"obowiązkowo zaimplementuj metodę spal_100")
    
    @abstractmethod
    def koszt_przejazdu(self,odl,litry,cena_l):
        raise NotImplementedError(f"obowiązkowo zaimplementuj metodę koszt_przejazdu")
