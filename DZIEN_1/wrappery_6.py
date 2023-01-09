import math
import time

def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        print(f'czas wykonania funkcji: {endtime-starttime} s')

    return wrapper

@pomiarczasu
def biglista():
    sum([i**3 for i in range(1000000)])

biglista()
