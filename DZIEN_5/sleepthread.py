import threading
import time

def p(i):
    for p in range(3):
        time.sleep(i+1)
        print(f'wątek #{i}\n')
        time.sleep(i)
    return

for i in range(3):
    t = threading.Thread(target=p, args=(i,))
    t.start()
    print(t)
