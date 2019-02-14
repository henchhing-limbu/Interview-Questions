# Given a list of numbers
# You want to sort the number based on frequency
# if a number has same frequency, just order by their time of occurence


# TODO: Get it done
from collections import OrderedDict
def sortByFreq(a):
	countA = OrderedDict.fromkeys(a)
	'''
	Ordered dic might help better to keep track of order they were inserted
	'''
	print(countA)
print(sortByFreq([2, 5, 2, 8, 5, 6, 8, 8]))
