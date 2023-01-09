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
