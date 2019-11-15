"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

# This problem is a back tracking problem.
# For this problem, we keep track of number of open and close parentheses to
# get the solutions.
# There are three cases we need to take care of:
# 1. If op_count == n then add p + (n-cp_count)*')'
# 2. If op_count < n then
#       p = p + '('
#       ...
# Better write the python code than this pseudocode.

def generate_parentheses(n):
    parentheses = []
    def backtracking(parenthesis, op_count, cp_count):
        if op_count == n:
            parentheses.append(parenthesis + (n-cp_count)*')')
            return
        if cp_count < op_count:
            backtracking(parenthesis + ')', op_count, cp_count + 1)
        backtracking(parenthesis + '(', op_count + 1, cp_count)
    
    backtracking('', 0, 0)
    return parentheses

print(generate_parentheses(3))

