# Algorithm:
# to get all subsets simply add the number to each subset of previous subset
# to get subset of n simply add the number to each subset of n-1

def findSubsets(nums):
	subsets = [[]]
	for i in range(len(nums)):
		size = len(subsets)
		for j in range(size):
			subsets.append(subsets[j] + nums[i])
	return subsets

