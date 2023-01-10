def czytaj_liste(lista):
    for i,j in enumerate(lista):
        print(f'-> element listy nr {i+1} -> {j}')
        
def czytaj_slownik(dictionary):
    for x,y in dictionary.items():
        print(f'klucz -> {x}: wartość -> {y}')
