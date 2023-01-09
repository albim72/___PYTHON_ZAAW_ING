#przypadek 1

def witaj(imie):
    return f'Miło Cię widzieć {imie}'

def konkurs(imie,punkty):
    return f"uczestnik {imie}, zdobył/a {punkty} pkt"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Olga",54))
