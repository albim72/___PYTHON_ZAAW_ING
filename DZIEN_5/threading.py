import os
import threading

def print_cube(liczba):
    print(f"sześcian liczby: {liczba**3}")

def print_square(liczba):
    print(f"kwadrat liczby: {liczba**2}")

def task1():
    print(f'Zadanie 1 przypisane do wątku: {threading.current_thread().name}')
    print(f'ID procesu biegnącego w pierwszym wątku: {os.getpid()}')

def task2():
    print(f'Zadanie 2 przypisane do wątku: {threading.current_thread().name}')
    print(f'ID procesu biegnącego w drugim wątku: {os.getpid()}')

if __name__ == '__main__':

    print(f'ID procesu dla programu głównego - main(): {os.getpid()}')
    print(f'Nazwa wątku głównego: {threading.current_thread().name}')

    t1 = threading.Thread(target=print_square,args=(10,))
    t2 = threading.Thread(target=print_cube,args=(10,))
    t3 = threading.Thread(target=task1,name='t1')
    t4 = threading.Thread(target=task2,name='t2')

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("wątki wykonano!")
