#przypadek 1
def liczby():
    for i in range(17):
        yield i

for p in liczby():
    print(p)

#przypadek 2
def wznowienie(n,k):
    print("wstrzymanie działania")
    yield 1001
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n+k
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n-k
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n*k
    print("wznowienie działania")

def gn(h):
    return h*2
for i in wznowienie(3,4):
    if i == 1001:
        continue
    print(f'wartość {gn(3)}')
    print(f'zwrócono wartość: {i}')

#przypadek 3
def genret():
    for i in range(11):
        if i==7:
            print("przerwanie")
            return 
        else:
            yield i

for t in genret():
    print(t)
