print((lambda e:e**3)(5))

h = 7
b = lambda u,z=h:u-2*z
print(b(7,2))
print(b(7))

def multi(n):
    return lambda a:a*n

print(multi(6)(9))


num = [0,4,6,17,-8,177,10,-4,78,13,0,1,1,1,5,6,200,9]

nbparz = list(filter(lambda x:x%2==0,num))
print(nbparz)

def fil(x):
    return x%2==0

nbparz2 = list(filter(fil,num))
print(nbparz2)

cube = list(map(lambda x:x**3,num))
print(cube)

#funkcje wyższego rzędu
def filtrowanie(dane,test):
    plus = []
    for element in dane:
        if(test(element)):
            plus.append(element)
    return plus

def ekstra_liczba(n):
    return n>=100

print(filtrowanie(num,ekstra_liczba))


def mapowanie(dane,transformacja):
    mapa=[]
    for element in dane:
        mapa.append(transformacja(element))
    return mapa

def add_five(n):
    return n+5

print(mapowanie(num,add_five))
