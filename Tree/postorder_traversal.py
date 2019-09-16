"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Recursive
def postorder_traversal(root):
	vals = []
	_postorder_traversal(root, vals)
	return vals

def _postorder_traversal(node, vals):
	if not node:
		return
	_postorder_traversal(node.left, vals)
	_postorder_traversal(node.right, vals)
	vals.append(node.val)

# Iterative
def postorder_traversal_iterative(root):
	vals = []
	nodes = []
	while True:
		# Loops down to leftmost node; stores parent on top of right child
		# for every level.
		while root:
			if root.right:
				nodes.append(root.right)
			nodes.append(root)
			root = root.left
		
		root = nodes.pop()
		
		# Check if there is a right subtree and whether the right subtree
		# has been processed yet. If not, make sure right child is processed
		# before root.
		if root.right and root.right == nodes[-1]:
			stack.pop()
			stack.append(root)
			root = root.right
		else: # If the right subtree is already processed.
			vals.append(root.val)
			root = None
		if not nodes:
			break
	return vals
