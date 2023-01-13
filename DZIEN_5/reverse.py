from collections import deque

#odwracanie wartości str za pomocą stosu

def reverse(s):
    stack = deque(s)
    return ''.join(stack.pop() for _ in range(len(s)))

if __name__ == '__main__':
    s = 'odwracanie znaków ciągu string'
    s = reverse(s)
    print(s)
