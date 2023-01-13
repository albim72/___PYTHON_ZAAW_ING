from collections import Counter,defaultdict, ChainMap

print("____ licznik _____")
seq1 = ['B','B','A','B','C','A','B','B','A','C']
seq2 = {'A':13,'B':4,'C':2}

print(Counter(seq1))
print(Counter(seq2))

print(Counter(A=5,B=7,C=1))

print("____domyślny słownik____")

d = defaultdict(int)

L = [1,2,3,4,2,4,6,7,8]

for i in L:
    d[i] += 1

print(d)

print("____ChainMap____")

d1 = {'a':4, 'b':7}
d2 = {'c':5, 'd':2}
d3 = {'e':11, 'f':4}

c = ChainMap(d1,d2,d3)
print(c)

print(c['a'])
print(c.values())
print(c.keys())
print(c.items())
print("__________________")
for h in c.values():
    print(h)

print("__________________")
for h in c.keys():
    print(h)

print("__________________")
for h,k in c.items():
    print(f'{h}: {k}')

