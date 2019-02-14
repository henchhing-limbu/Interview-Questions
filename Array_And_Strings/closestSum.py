# This function takes an array of integers as well as a target number
# Returns a pair of numbers as a tuple whose sum is closest to the target

def closestSum(a, target):
    sortedArr = sorted(a)
    i, j = 0, len(a) - 1
    bestSumm = float('inf')
    result = (None, None)
    while i < j:
        summ = sortedArr[i] + sortedArr[j]
        if abs(bestSumm - target) > abs(summ - target):
            bestSumm = summ
            result = (sortedArr[i], sortedArr[j])
            
        if summ > target:
            j -= 1
        else:
            i += 1
    return result
