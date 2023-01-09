#przypadek 1
def liczby():
    for i in range(17):
        yield i

for p in liczby():
    print(p)
