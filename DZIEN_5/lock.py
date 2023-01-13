from threading import Thread,Lock
from time import sleep

counter = 0
def increase(by,lock):
    global counter
    lock.acquire()

    local_counter = counter
    local_counter +=by
    sleep(0.1)
    counter = local_counter
    print(f'counter = {counter}')
    lock.release()

lock = Lock()
t1 = Thread(target=increase,args = (1000000,lock))
t2 = Thread(target=increase,args = (2000000,lock))
t3 = Thread(target=increase,args = (3000000,lock))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(f'final counter:{counter}')
