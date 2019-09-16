"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Recursive
def inorder_traversal(root):
	vals = []
	_inorder_helper(root, vals)
	return vals

def _inorder_helper(node, vals):
	if not node:
		return
	_inorder_helper(node.left, vals)
	vals.append(node.val)
	_inorder_helper(node.right, vals)

# Iterative
def inorder_traversal_iterative(root):
	vals = []
	nodes = []
	curr = root
	while True:
		if curr:
			nodes.append(curr)
			curr = curr.left
		elif nodes:
			curr = nodes.pop()
			vals.append(curr.val)
			curr = curr.right
		else:
			break
	return vals
		if node:
			nodes.append(
