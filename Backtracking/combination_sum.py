"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

# The template used here can be used for most of the combiantion problems.
# You have a solution set to keep track of different combinations we want.
# You have search method() that looks for different combiantions.
# You have candidates() method that returns search space for given stage.
# You have is_valid() method that checks if a solution is valid or not


def is_valid(s, target):
    return sum(s) == target

def candidates(nums, s, target):
    rem = target - sum(s)
    return [num for num in nums if num <= rem]

def search(nums, s, target, solutions):
    if is_valid(s, target):
        solutions.add(tuple(sorted(list(s))))

    for num in candidates(nums, s, target):
        s.append(num)
        search(nums, s, target, solutions)
        s.pop()
    
def combination_sum(candidates, target):
    solutions = set()
    s = []
    search(candidates, s, target, solutions)
    return [list(solution) for solution in solutions]

solutions = combination_sum([2, 3, 6, 7], 7)
solutions = combination_sum([2, 3, 5], 8)
