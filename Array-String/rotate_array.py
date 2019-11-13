def rotateArray(arr, k):
    # look for edge cases
    if k < 1 or arr == []:
        return arr
    return arr[-k:] + arr[:-k]

def rotate_array_inplace(arr, k):
	if k < 0 or k > len(arr):
		return
	reverse_array(arr, 0, len(arr) - 1 - k)
	reverse_array(arr, len(arr) - k, len(arr) - 1)
	reverse_array(arr, 0, len(arr) - 1)

def reverse_array(arr, i, j):
	while i < j:
		arr[i], arr[j] = arr[j], arr[i]
		i += 1
		j -= 1

assert rotateArray([1,2,3,4,5], 2) == [4, 5, 1, 2, 3]
assert rotateArray([],2) == []
assert rotateArray([1,2],0) == [1, 2]

arr1 = [1, 2, 3, 4, 5]
arr2 = []
arr3 = [1, 2]

rotate_array_inplace(arr1, 2)
rotate_array_inplace(arr2, 2)
rotate_array_inplace(arr3, 0)

assert arr1 == [4, 5, 1, 2, 3]
assert arr2 == []
assert arr3 == [1, 2]
# This can be done inplace 
# reverse the first half of the array
# reverse the second half of the array
# reverse the whole array
