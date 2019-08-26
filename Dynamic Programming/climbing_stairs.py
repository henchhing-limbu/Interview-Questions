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

"""
Instead of 1 or 2 steps to take a time, you are given a list of possible steps
you can take.
"""
def num_of_ways_to_climb(n, steps):
	num_possible_ways = [-1] * (n + 1)
	# This is sorta like base case. If there are no stairs to climb, there can
	# only be one possible way.
	num_possible_ways[0] = 1
	for i in range(1, n+1):
		possible_ways_i = [num_possible_ways[i-j] for j in steps if i-j >= 0]
		if possible_ways_i:
			# using already calculated values, update the current stiair step.
			num_possible_ways[i] = sum(possible_ways_i)
	return num_possible_ways[-1]
print(num_of_ways_to_climb(3, [1, 3, 2]))
		
