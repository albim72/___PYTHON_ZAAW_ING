from queue import Queue

q = Queue(maxsize=5)
print(q.qsize())
q.put(454)
q.put(656)
q.put(244)
q.put(865)
q.put(624)
print(q.qsize())

print(f'full: {q.full()}')

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())

print(f'kolejka pusta: {q.empty()}')
