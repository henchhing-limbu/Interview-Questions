"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# This is a simple tree traversal question. While you traverse down towards
# leaf, pass the sum of node values from root to the current node so that
# when you reach leaf, you have the sum of root-to-that-leaf path. Then,
# simply check if this is equal to the target sum.

def has_path_sum(root, target):
    if not root:
        return False
    
    if not (root.left or root.right):
        return target == 0
    else:
        return has_path_sum(root.left, target-root.val) or has_path_sum(
                root.right, target-root.val)
