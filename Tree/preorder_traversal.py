"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Recurvise solution
def preorder_traversal(root):
	vals = []
	_preorder_helper(root, vals)
	return vals

def _preorder_helper(node, vals):
	if not node:
		return
	vals.append(node.val)
	_preorder_helper(node.left, vals)
	_preorder_helper(node.right, vals)


# Iterative solution
def preorder_traversal_iterative(root):
	vals = []
	nodes = [root]
	while nodes:
		node = nodes.pop()
		if node:
			vals.append(node.val)
			nodes.append(node.right)
			nodes.append(node.left)
	return vals
