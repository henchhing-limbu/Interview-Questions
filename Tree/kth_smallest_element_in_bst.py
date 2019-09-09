"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
"""

from binaryTree import BinaryTree

def get_kth_smallest(root, k):
	if not root or k < 1:
		return None
	return _get_kth_smallest_helper(root, k, 0)[1].val

def _get_kth_smallest_helper(root, k, pos):
	if not root:
		return (False, None, pos)

	# Get the result from left child
	left_result = _get_kth_smallest_helper(root.left, k, pos)
	# Check if you have already found the result
	if left_result[0]:
		return left_result
	else:
		# Update the position and see if it's kth smallest node.
		# If so, return the True value.
		pos = left_result[2] + 1
		if pos == k:
			return (True, root, pos)
	# Get the result from the right child.
	return _get_kth_smallest_helper(root.right, k, pos)

tree = BinaryTree(3)
tree.insert(1)
tree.insert(4)
tree.insert(2)

assert get_kth_smallest(tree.root, 1) == 1

tree = BinaryTree(5)
tree.insert(3)
tree.insert(2)
tree.insert(6)
tree.insert(4)
tree.insert(1)

assert get_kth_smallest(tree.root, 3) == 3
