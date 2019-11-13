"""
Given a list of integers and a target k, find if there exists a subset in the
list whose sum is equal to k.

For example:
    Input: [2, 3, 7, 8, 10]
    k = 11
    Output: True as [3, 8] sums to 11
    
    Input: [2, 3, 7, 8, 10]
    k = 14
    Output: False as there is no subset that sums to 14
"""

def subset_sum(nums, k):
    nums.sort()
    dp_table = [[False]*
