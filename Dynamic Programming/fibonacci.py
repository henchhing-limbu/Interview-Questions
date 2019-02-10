import time

# using recursion
def recFibonacci(n):
	if n <= 0:
		return 0
	if n == 1:
		return 1
	return recFibonacci(n-1) + recFibonacci(n-2)

# bottom up
def botFibonacci(n):
	if n <= 0:
		return 0
	a, b = 0, 1
	for i in range(2, n+1):
		temp = b
		b = a + b
		a = temp
	return b

		
print("NUMBER: 20")
num = 20
print("Recursive solution: ")
startTime = time.time()
print(recFibonacci(num))
endTime = time.time()
print(endTime - startTime)

print("BottomUp solution: ")
startTime = time.time()
print(botFibonacci(num))
endTime = time.time()
print(endTime - startTime)
