def missingNumber(a, n):
	sum1 = sum(a)
	sum2 = (n*(n+1)) >> 1
	return sum2 - sum1
print(missingNumber([1,2,3,5], 5))

def missinNumberII(a, n):
	X, Y = 0, 0
	for i in range(n):
		X ^= i
	for j in a:
		Y ^= j
	return X^Y
	
