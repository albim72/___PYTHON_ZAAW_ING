#silnia n!=1*2*3*...*n, n jest liczbą natualną(z uwzględnieniem 0)
#double max 1.8E308
#n??? 171!

import sys

sys.set_int_max_str_digits(0x1000000)
sys.setrecursionlimit(0x1000000)
1
def silnia(n):
    if n<0:
        raise ValueError("silnia nie jest zdefiniowana dla liczb ujemnych")
    wynik = 1
    for i in range(1,n+1):
        wynik*=i
    return wynik

def silnia_rek(n):
    if n < 0:
        raise ValueError("silnia nie jest zdefiniowana dla liczb ujemnych")
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n=int(input("podaj wartość atrybutu n: "))
    print(f'silnia z n = {n} wynosi: {silnia(n)}')
    print(f'silnia rekurencyjna z n = {n} wynosi: {silnia_rek(n)}')
except ValueError as d:
    print(d)
except:
    print("nieokreślony błąd!")
    raise
