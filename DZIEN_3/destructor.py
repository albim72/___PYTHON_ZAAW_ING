class Pracownik:
    def __init__(self):
        print("pracownik został utworzony")

    def info(self):
        print("pracownik firmy ABC")

    def __del__(self):
        print("destruktor został wywołany, pracownik zosotał usunięty...")

pr = Pracownik()
pr.info()
pr.info()
pr.info()

del pr

def tworzenie_pracownika():
    print("utworzenie nowego pracownika...")
    nowyprac = Pracownik()
    print("pracownik został utworzony! -- info z funckji")
    return nowyprac
print("________________________________________")
np = tworzenie_pracownika()
np.info()
del np
print("ciąg dalszy")
print("__________________________________")
nowy = Pracownik()
nowy.info()

nowy = Pracownik()
nowy.info()

