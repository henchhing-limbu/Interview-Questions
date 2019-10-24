"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

def is_valid(nums, k, n):
    """Check if the combination of numbers sums to n and their count is k."""
    return len(nums) == k and sum(nums) == n

def candidates(nums, n):
    """Return list of candidates that leads to new sub-solution state."""
    rem = n - sum(nums)
    return [num for num in range(1, 10) if num <= rem and num not in nums]

def search(nums, k, n, solutions):
    if is_valid(nums, k, n):
        solutions.add(tuple(nums))

    for num in candidates(nums, n):
        nums.add(num)
        search(nums, k, n, solutions)
        nums.remove(num)

def solve(k, n):
    solutions = set()
    nums = set()
    search(nums, k, n, solutions)
    return [list(solution) for solution in solutions]

assert sorted(solve(3, 7)) == sorted([[1, 2, 4]])
assert sorted(solve(3, 9)) == sorted([[1, 2, 6], [1, 3, 5], [2, 3, 4]])
