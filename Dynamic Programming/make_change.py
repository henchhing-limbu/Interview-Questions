"""
Given a value V, if we want to make change for V cents, and we have infinite
supply of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum
number of coins to make the change?

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents 

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents

"""
def find_min_coins(cents, coins):
	min_coins = [-1] * (cents + 1)
	min_coins[0] = 0
	for i in range(1, cents + 1):
		num_of_possible_changes = [
			min_coins[i-j] for j in coins if i - j >= 0 and min_coins[i-j] >= 0]
		if num_of_possible_changes:
			min_coins[i] = 1 + min(num_of_possible_changes)
	return min_coins[-1]

print(find_min_coins(30, [25, 10, 5]))
print(find_min_coins(11, [9, 6, 5, 1, 1]))
print(find_min_coins(2, [5, 10]))
	
	
