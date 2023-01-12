import time

def find_prime_numbers_sum(minimum,maximum):
    total = 0
    for number in range(minimum,maximum+1):
        count = 0
        for i in range(2,(number//2+1)):
            if number%i == 0:
                count=count+1
                break
        if count == 0 and number!=1:
            total = total + number

    return total

numbers = [(1,10000),(3,50000),(5000,100000),(4,900),(800,15000)]

start_time = time.time()
for pair in numbers:
    prime_sum = find_prime_numbers_sum(*pair)
    print(prime_sum)

end_time = time.time()

print(f'czas całkowity wyznaczenia sum liczb pierwszych -> {end_time - start_time:.2f} s')
