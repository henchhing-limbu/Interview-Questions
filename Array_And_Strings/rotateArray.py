def rotateArray(arr, k):
    # look for edge cases
    if k < 1 or arr == []:
        return "Can't rotate"
    return arr[-k:] + arr[:-k]

print(rotateArray([1,2,3,4,5], 2))
print(rotateArray([],2))
print(rotateArray([1,2],0))
