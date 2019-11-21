"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

# This is simple bit manipulation problem.
# keep takeaway is XOR of same integer values results in 0

def single_number(nums):
    single_num = 0
    for num in nums:
        single_num ^= num
    return single_num

assert single_number([2, 2, 1]) is 1
assert single_number([4, 1, 2, 1, 2]) is 4
