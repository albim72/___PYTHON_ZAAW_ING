#przypadek 1

def h(x):
    return x**3

n=100
def policz(a,b,c,y):
    global n
    n = (a+b)*c+y + n
    m = n+h(b)
    return m

print(policz(2,4,3,5))
print(n)

#przypadek 2

def bx(n,m=1,k=4,f=2):
    return math.sqrt(n+m) -k*f

print(bx(12,7,8,3))
print(bx(12,7,8))
print(bx(12,7))
print(bx(12))
print(bx(5,6,f=7))
