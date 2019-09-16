"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

# The idea is similar to sell_stock_ii
# We simply need to keep track of two highest profits that can be made from
# buying and selling of stocks.

def sell_stock_iii(prices):
	if not prices:
		return 0
	profit1, profit2 = 0, 0
	buy_price, sell_price = prices[0], float('-inf')
	for price in prices:
		if price > sell_price:
			sell_price = price
		else:
			profit = sell_price - buy_price
			buy_price, sell_price = price, price
			profit1, profit2 = _update_profits(profit, profit1, profit2)
	if sell_price > buy_price:
		profit1, profit2 = _update_profits(sell_price - buy_price, profit1, profit2)
	return profit1 + profit2

def _update_profits(profit, profit1, profit2):
	if profit1 <= profit <= profit2:
		profit1 = profit
	elif profit > profit2:
		profit1, profit2 = profit2, profit
	return profit1, profit2

assert sell_stock_iii([1, 2, 3, 4, 5]) is 4
assert sell_stock_iii([3, 3, 5, 0, 0, 3, 1, 4]) is 6
assert sell_stock_iii([7, 6, 4, 3, 1]) is 0
assert sell_stock_iii([1, 5, 2, 3, 5]) is 7
assert sell_stock_iii([1, 5, 4,3, 2, 1]) is 4
