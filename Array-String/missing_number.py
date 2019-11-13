# Given a list of numbers. The actual numbers are from 1 to n. However, the
# array has one missing number from the range. Find the missing number.

def missingNumber(a, n):
	sum1 = sum(a)
	# Use the arithmetic sum formula to get sum of the numbers.
	sum2 = (n*(n+1)) >> 1
	return sum2 - sum1

def missinNumberII(a, n):
	X, Y = 0, 0
	for i in range(n):
		X ^= i
	for j in a:
		Y ^= j
	# The difference between X and Y is the missing number. XOR between
	# X and Y must return the missing number
	return X^Y

assert missingNumber([1,2,3,5], 5) == 4
assert missingNumber([1,2,4,5], 5) == 3
	
