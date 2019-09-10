"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
"""

# This problem can be solved using Dynamic programming.
# We can create a list that stores the longest increasing subsequence for each
# subarray. So, when other problems want to compute the longest increasing
# subsequence for these subarrays, we can simply look into the list making it
# dynamic programming.

def length_of_lis(nums):
	lengths = [0] * len(nums)
	lengths[0] = 1
	for i in range(1, len(nums)):
		length_of_is = 1
		for j in range(i):
			# Find the subarray with longest length and whose last element is
			# smaller than current element. Store the length of longest
			# incresing subsequence with current element in lengths.
			if nums[j] < nums[i]:
				length_of_is = max(length_of_is, lengths[j]+1)
		lengths[i] = length_of_is
	return max(lengths)

assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) is 4	
assert length_of_lis([2, 10, 5, 18, 9, 1]) is 3
			
