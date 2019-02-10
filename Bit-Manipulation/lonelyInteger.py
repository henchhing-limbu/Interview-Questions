# Valid array is provided
def lonelyInteger(a):
	lonelyInt = 0
	for num in a:
		lonelyInt ^= num
	return lonelyInt

print(lonelyInteger([3,2,7,4,3,2,7]))
