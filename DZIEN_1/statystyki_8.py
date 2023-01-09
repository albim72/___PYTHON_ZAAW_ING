liczby = [56,1009,45,-660,0,34,156,778,1990,-1080,190,211,59,689,999]

def pokaz_stat(lista):
    minimum = min(lista)
    maksimum = max(lista)
    liczba_elem = len(lista)
    sumaelem = sum(lista)
    rozstep = maksimum - minimum
    avg = sumaelem/liczba_elem
    return minimum,maksimum,liczba_elem,sumaelem,rozstep,avg

wynik = pokaz_stat(liczby)
print(wynik)

mini,maxi,lbel,sumel,roz,avg = pokaz_stat(liczby)
print(f'wartość największa: {maxi}, wartość najmniejsza: {mini}, liczba elementów: {lbel}, '
      f'suma elementów: {sumel}, rozstęp danych: {roz}, średnia arytmetyczna: {avg:.2f}')
