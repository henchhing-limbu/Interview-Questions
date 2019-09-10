"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
"""

# This is a simple dynamic programming problem.
# We go through money unit 1 to given amount. We find fewest number of coins
# needed to make up for each amount. As we go from 1 to amount, we can use the
# subproblems to compute the problem.

def coin_change(coins, amount):
	num_of_coins = [-1] * (amount+1)
	num_of_coins[0] = 0

	for i in range(1, amount+1):
		num_of_coins_i = []
		# Find minimum coins required using each possible coin.
		# Take minimum of these minimum coins as the optimal value for this
		# subproblem.
		for coin in coins:
			# Keep track of num of coins if change is possible.
			if i >= coin and num_of_coins[i-coin] >= 0:
				num_of_coins_i.append(num_of_coins[i-coin])
		if num_of_coins_i:
			num_of_coins[i] = min(num_of_coins_i) + 1
	return num_of_coins[-1]

assert coin_change([1, 2, 5], 11) is 3
assert coin_change([2], 3) is -1
