print((lambda e:e**3)(5))

h = 7
b = lambda u,z=h:u-2*z
print(b(7,2))
print(b(7))

def multi(n):
    return lambda a:a*n

print(multi(6)(9))
