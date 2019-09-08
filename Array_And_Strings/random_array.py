from random import randint

# Go through each element of the array and find a random index between the
# current element index and the last index of the array. Swap the element
# at random index and current element.
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

arr = [1,2,3,4,5]
orderArrRand(arr)
print(arr)
