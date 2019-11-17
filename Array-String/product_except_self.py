"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

# To compute product of the numbers in the array without number at index i, we
# need the product of all the numbers on left side and product of all the
# numbers on the right side.
# We simply keep track of consecutive products from left to right
# and right to left

def product_except_self(nums):

