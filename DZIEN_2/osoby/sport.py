class Sport:
    def __init__(self,dyscyplina:str,lataupr:int,best_wynik:str):
        self.dyscyplina = dyscyplina
        self.lataupr = lataupr
        self.best_wynik = best_wynik

    def infosport(self) -> str:
        return f'{self.dyscyplina}, lata uprawiania: {self.lataupr}, życiówka: {self.best_wynik}'

class Ekstra:
    pass

