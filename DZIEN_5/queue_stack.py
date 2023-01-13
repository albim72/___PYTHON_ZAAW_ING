print('_________ kolejka  _______________')
queue = []
queue.append('Tarnów')
queue.append('Kraków')
queue.append('Gdańsk')

print("inicjacja kolejki")
print(queue)
print("elementy zdjęte z kolejki\n")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("kolejka po zdjęciu elementów")
print(queue)

print('_________ stos  _______________')

stack = []
stack.append('Tarnów')
stack.append('Kraków')
stack.append('Gdańsk')

print("inicjacja stosu")
print(stack)
print("elementy zdjęte ze stosu\n")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("stos po zdjęciu elementów")
print(stack)
