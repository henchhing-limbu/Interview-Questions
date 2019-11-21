"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""

# use two variable to keep track of seen once and seen twice.
# seen_once = ~seen_twice & (seen_once ^ x)
# seen_twice = ~seen_once & (seen_twice ^ x)

def single_number(nums):
    seen_once, seen_twice = 0, 0
    for num in nums:
        seen_once = ~seen_twice & (seen_once ^ num)
        seen_twice = ~seen_once & (seen_twice ^ num)
    return seen_once

assert single_number([2, 2, 3, 2]) is 3
assert single_number([0, 1, 0, 1, 0, 1, 99]) is 99
