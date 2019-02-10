
def makeChange(money, coins):
	

def makeChangeHelper(money, coin, mem, index):
	if money == 0:
		return 1
	if index >= len(coin):
		return 0
	
	key = money + "-" + index
	if key in mem:
		return mem[key]

	
	
