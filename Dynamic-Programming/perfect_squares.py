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

# The first thing that came to my find when trying to solve this problem is
# try to get the biggest perfect square 'x1' less than n. Then, get the biggest
# perfect square 'x2' less than n - x1. Continue this until target gets to 0.
# This is a greedy approach. 
# n = 13
# count = 0

# Takes x = 9
# n = 13 - 9 = 4
# count = 1

# Takes x = 4
# n = 4 - 4 = 0
# count = 2

# number of perfect squares needed = 2
# Seems to work.

# However, the problem with this can be seen with this counterexample.
# Take n = 12
# count = 0

# greed approach takes x = 9
# n = 12 - 9 = 3
# count = 1

# takes x = 1
# n = 3-1 = 2
# count = 2
# ...
# takes x = 1
# n = 1-1 = 0
# count = 4

# However the right answer is 3 which we get by 4 + 4 + 4.

# This can be seen as knapsack problem which can be solved using dynamic
# programming.

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
