"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
"""

def evaluate_rpn(tokens):
	operands = []
	for token in tokens:
		if token in '/+-*':
			operand1, operand2 = operands.pop(), operands.pop()
			if token == '/':
				operands.append(int(operand2 / operand1))
			elif token == '+':
				operands.append(operand2 + operand1)
			elif token == '-':
				operands.append(operand2 - operand1)
			else:
				operands.append(operand2 * operand1)
		else:
			operands.append(str_to_int(token))
	return operands.pop()

def str_to_int(s):
	"""Converts the string number to integer."""
	if s[0] == '-':
		return -1 * int(s[1:])
	return int(s)

arr1 = ['2', '1', '+', '3', '*']
arr2 = ['4', '13', '5', '/', '+']
arr3 = ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']
assert evaluate_rpn(arr1) == 9
assert evaluate_rpn(arr2) == 6
assert evaluate_rpn(arr3) == 22
