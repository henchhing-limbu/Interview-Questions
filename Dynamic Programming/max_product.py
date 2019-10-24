"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

# This is similar to maximum sum subarray problem.
# We keep track of maximum product and minimum product
# We do this because minimum product when multipled by a negative integer can
# lead to maximum product.

def max_product(nums):
    if not nums:
        return 0
    max_product, min_product, result = nums[0], nums[0], nums[0]
    for num in nums[1:]:
        if num > 0:
            max_product = max(num, num * max_product)
            min_product = max(num, num * min_product)
        else:
            max_product = max(num, num * min_product)
            min_product = min(num, num * max_product)
        result = max(max_product, result)
    return result

assert max_product([2, 3, -2, 4]) == 6
assert max_product([-2, 0, -1]) == 0
assert max_product([]) == 0
