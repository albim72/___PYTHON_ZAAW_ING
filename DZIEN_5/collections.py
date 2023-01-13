from collections import Counter,defaultdict, ChainMap,UserString

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

print("__________UserString_________")

class MojString(UserString):
    def append(self,s):
        self.data += s

    def remove(self,s):
        self.data = self.data.replace(s,"")

s1 = MojString("Bieganie Ultra")
print(f"tekst oryginalny: {s1.data}")

s1.append(" w górach")
print(f"tekst po dodaniu frazy: {s1.data}")

s1.remove('Ultra ')
print(f"tekst po usunięciu frazy: {s1.data}")

s2 = MojString("hehehehehehehehe")
print(f"tekst oryginalny: {s2.data}")

s2.append(" - ale ubaw")
print(f"tekst po dodaniu frazy: {s2.data}")

s2.remove('h')
print(f"tekst po usunięciu frazy: {s2.data}")

