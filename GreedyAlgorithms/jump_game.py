"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

# This is simply a greed algorithm problem.

# The logic is simple. From any given position, we want to find if there is any
# position you can jump to that leads to the last index.

# We come from right to left and see for each position if there is a position
# in the right we can jump to that leads to last index. To keep track of the
# position that can lead to last index, we will use a variable. And, for any
# position that can jump to the variable or beyond that can reach the last
# index.

def can_jump(nums):
    good_position = len(nums) - 1
    for i in range(len(nums)-2, -1, -1):
        if i + nums[i] >= good_position:
            good_position = i
    return True if good_position == 0 else False

assert can_jump([2, 3, 1, 1, 4]) is True
assert can_jump([3, 2, 1, 0, 4]) is False
