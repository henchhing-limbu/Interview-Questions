"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# Recursive method
def is_symmetric(root):
	return is_symmetric_helper(root, root)

def is_symmetric_helper(node1, node2):
	if node1 is None and node2 is None:
		return True
	if node1 is None or node2 is None or node1.val != node2.val:
		return False
	return is_symmetric_helper(node1.left, node2.right) and is_symmetric_helper(node1.right, node2.left)

# Iterative method
from collections import deque
def is_symmetric_iterative(root):
	queue = deque()
	queue.append(root)
	queue.append(root)
	while queue:
		node1, node2 = queue.pop(), queue.pop()
		if node1 is None and node2 is None:
			continue
		if node1 is None or node2 is None or node1.val != node2.val:
			return False
		queue.append(node1.left)
		queue.append(node2.right)
		queue.append(node1.right)
		queue.append(node2.left)
	return True
