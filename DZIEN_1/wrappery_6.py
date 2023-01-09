import math
import time

def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        print(f'czas wykonania funkcji: {endtime-starttime} s')

    return wrapper

def sleep(funkcja):
    def wrapper():
        time.sleep(1)
        return funkcja()
    return wrapper


@sleep
@pomiarczasu
def biglista():
    sum([i**3 for i in range(1000000)])

biglista()


lt = [i**3+100 for i in range(10000000)]

@pomiarczasu
def biglista_sec():
    sum(lt)

biglista_sec()

#dekorator z użyciem funkcji magicznej __name__

def debug(funkcja):
    def wrapper(*args):
        print(f'wołana funkcja: {funkcja.__name__}')
        funkcja(*args)
    return wrapper

@debug
def info(msg):
    print(f"ważna informacja: {msg}")

info("dokument 56466456")

#repeater
def repeater(n):
    def wrapper(funkcja):
        def inner(*args):
            for i in range(n):
                funkcja(*args)
        return inner
    return wrapper

@repeater(n=6)
def komunikat(k,n):
    print(f'ważny komunikat nr {n}: {k}')

komunikat("Ala ma kota",22)
