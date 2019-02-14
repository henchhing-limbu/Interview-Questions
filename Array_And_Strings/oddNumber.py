# Given an array of numbers where a number has odd number of counts
# You are supposed to get the number
# Use of XOR
def oddNumber(a):
	oddNum = 0
	for num in a:
		oddNum ^= num
	return oddNum
