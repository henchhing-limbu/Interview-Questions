'''

There exists a staircase with N steps, and you can climb up either 1 or 2 steps
at a time. Given N, write a function that returns the number of unique ways you
can climb the staircase. The order of the steps matters.

'''

def num_steps(n):
	if n < 1:
		return 0
	if n == 1:
		return 1
	
	num_steps_2 = 1
	num_steps_1 = 2
	
	for _ in range(n - 2, 0, -1):
		num_steps_1, num_steps_2 = num_steps_2 + num_steps_1, num_steps_1

	return num_steps_1

print(num_steps(2))
