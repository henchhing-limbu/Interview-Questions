"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

def is_subtree(s, t):
	if s is None:
		return _is_subtree_helper(s, t)
	return _is_subtree_helper(s, t) or is_subtree(s.left, t) or is_subtree(s.right, t)

def _is_subtree_helper(node1, node2):
	if node1 is None and node2 is None:
		return True
	if node1 is None or node2 is None or node1.val != node2.val:
		return False
	return _is_subtree_helper(node1.left, node2.left) and _is_subtree_helper(node1.right, node2.right)


