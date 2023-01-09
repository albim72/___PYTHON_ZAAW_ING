#przypadek 1

def witaj(imie):
    return f'Miło Cię widzieć {imie}'

def konkurs(imie,punkty):
    return f"uczestnik {imie}, zdobył/a {punkty} pkt"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Olga",54))

#przypadek 2

def rejestracja(oplata):
    def lista():
        return "jesteś na liście zawodników - opłacony"
    def brak():
        return "dokonaj wpłaty w ciągu 3 dni"
    def error():
        return "zły kod wpłaty (0-brak,1-wpłata)"

    if oplata==1:
        return lista
    elif oplata==0:
        return brak
    else:
        return error


print(rejestracja(1)())
print(rejestracja(0)())
print(rejestracja(15)())


#przypadek 3
def startstop(funkcja):
    def wrapper(*args):
        print("startowanie procesu")
        funkcja(*args)
        print("kończenie procesu...")
    return wrapper


def zawijanie(czego):
    print(f'zawijanie {czego} w sreberka')

zw = startstop(zawijanie)
zw("czekoladek")

zawijanie("cukierków")

@startstop
def dmuchanie(czego):
    print(f'dmuchanie {czego} na urodziny')

dmuchanie("baloników")

