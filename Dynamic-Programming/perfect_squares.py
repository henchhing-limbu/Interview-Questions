"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

# This can be solved using dynamic programming.

import math

def num_squares(n):
	result = [float('inf')] * (n+1)
	result[1] = 1
	for i in range(2, n+1):
		for j in range(1, int(math.sqrt(i)) + 1):
			square = j**2
			if square == i:	# Best case scenario where i is perfect square.
				result[i] = 1
			else:
				# Since we are iterating from left to right result[i-j**2]
				# value would already be computed. The subproblem is already
				# solved and we are using that subproblem to solve current
				# problem.
				result[i] = min(result[i], result[i-j**2] + 1)
	return result[-1]

assert num_squares(12) is 3
assert num_squares(13) is 2	
