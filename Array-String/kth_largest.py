"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""

# This can be done using a max heap of size k.
# The time complexity is O(nlogk) where n is the size of array and k is the
# input k.

# This can be implemented using a technique similar to quicksort as well.
# This technique is also called order statistic.
# Logic behind this:
# When we take a pivot and do the quicksort partition, we know how many
# elements are on either side of the pivot after the parititon loop. We can use
# this knowledge to know which side to look for and when to stop.

def get_kth_largest(nums, k):
	if len(nums) < k: return -1
	return _get_kth_largest_helper(nums, k, 0, len(nums)-1)

def _get_kth_largest_helper(nums, k, start, end):
	left = start
	i = left - 1
	pivot = nums[end]

	while left < end:
		if nums[left] >= pivot:
			i += 1
			nums[i], nums[left] = nums[left], nums[i]
		left += 1
	nums[i+1], nums[end] = nums[end], nums[i+1]
	if i+1 == k-1:
		return pivot
	elif i+1 < k-1:
		return _get_kth_largest_helper(nums, k, i+2, end)
	else:
		return _get_kth_largest_helper(nums, k, start, i)

assert get_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
assert get_kth_largest([9, 2, 10, 8, 17, 5], 4) == 8	
