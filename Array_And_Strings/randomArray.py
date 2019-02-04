from random import randint
def orderArrRand(a):
    if not a:
        return
    
    i, length = 0, len(a) - 1
    while i < length:
        j = randint(i, length)
        swap(a, i, j)
        i += 1
    
def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


