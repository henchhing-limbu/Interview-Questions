# This functions returns the maximum difference between two numbers in 
# input array where the number should come before second in the array

# returns -inf if the numbers are in descending order
def maxDiff(a):
    diff = float('-inf')
    x = 0
    for i in range(1, len(a)):
        localDiff = a[i] - a[x]
        if localDiff >= 0 and localDiff > diff:
            diff = localDiff
        if a[i] < a[x]:
            x = i
        
    return diff

print(maxDiff([-1, -2, -3]))
