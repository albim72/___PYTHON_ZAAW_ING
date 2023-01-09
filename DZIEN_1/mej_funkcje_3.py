#przypadek 1
import math

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

#przypadek3

def rank(*lang,nrrank,**kwargs):
    print(f'ranking języków programowania:\n1: {lang[0]}\n2: {lang[1]}\n3: {lang[2]}.')

rank("Python","Java","C++",nrrank=3)
rank("Python","Java","JavaScript","C++","Perl",nrrank=3)
