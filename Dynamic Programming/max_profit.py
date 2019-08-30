"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
"""

def get_max_profit(prices):
	if not prices:
		return 0
	max_profit = 0
	min_stock, max_stock = prices[0], prices[0]
	for stock_price in prices[1:]:
		# If this is the minimum stock seen until now, then this should be the
		# minimum stock from now on. The old max stock is useless as you can't
		# sell stock back in time so it needs to be updated as well.
		if stock_price < min_stock:
			min_stock, max_stock = stock_price, stock_price
		elif stock_price > max_stock:
			max_stock = stock_price
			max_profit = max(max_stock - min_stock, max_profit)
	return max_profit,
