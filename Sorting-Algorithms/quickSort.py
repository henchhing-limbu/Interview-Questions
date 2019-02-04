def quickSort(a):
    quickSortHelper(a, 0, len(a)-1)
    
def quickSortHelper(a, i, j):
    while i < j:
        ind = partition(a, i, j)
        quickSortHelper(a, i, ind - 1)
        quickSortHelper(a, ind + 1, j)

def partition(a, i, j):
    print(a)
    pivot = a[j]
    ind = i - 1
    for x in range(i,j):
        if a[x] <= pivot:
            ind += 1
            a[ind], a[x] = a[x], a[ind]
    a[ind + 1], a[j] = a[j], a[ind + 1]
    return ind + 1

arr = [1,7,8,9,16,5]
quickSort(arr)
print(arr)
        
