"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

# The first idea that came to my mind is sliding window. However, because of
# the negative numbers in the list, this does not work.

# There is always the brute force to solve this proble. Just find all possible
# subarrays and check if the subarray sum equals target.
# The time complexity becomes O(n^3) as find all subarray takes O(n^2) and
# checking if the subarray sum equals target takes O(n) time.

# Optimization 1
# One way to optimize this would be to keep track of cumulitive sum. Say, we
# want to find sum of nums[i...j], then we can find the sum in constant time
# by cum_sum[j] - cum_sum[i].

def subarray_sum(nums, k):
    subarray_count = 0
    cumul_sum = 0
    for i in range(len(nums)):
        cumul_sum += nums[i]
        cumul_sum_j = 0
        for j in range(i+1):
            if cumul_sum_j == k:
                subarray_count += 1
            cumul_sum_j += nums[j]
    return subarray_count

# Optimization 2
# This sort of pattern in difficult to see if you haven't practiced a lof of
# interview questions. If cum_sum[i] == cum_sum[j] where j > i, this means that
# sum of subarray between i+1 ... j-1 is 0. This idea can be further expanded
# into if the difference between cum_sum[j] - cum_sum[i] == k, then the sum of
# subarrary i+1 ... j-1 is k.

# We will use a hash map to keep track of count of cumulitive sums because
# there can be many subarrays with same sum. So, we keep track of cumulitive
# sum while we iterate over the numbers. We increment the count of the 
# cumulitive sum in the map. We check if the differenec between current 
# cumulitive sum - k exists in the map. If it does, we add map[cs-k] value to
# number of possible subarrays.

from collections import defaultdict

def subarray_sum_optimized(nums, k):
    subarray_count, cs = 0, 0
    cs_map = defaultdict(int)
    cs_map[0] = 1
    for num in nums:
        cs += num
        subarray_count += cs_map[cs-k]
        cs_map[cs] += 1
    return subarray_count

assert subarray_sum_optimized([1, 1, 1], 2) is 2
assert subarray_sum_optimized([1], 0) is 0

