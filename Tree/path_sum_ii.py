"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

def find_root_to_leaf_paths(root, target):
    if not root:
        return []

    paths = []
    def find_path(node, path_nodes):
        path_nodes.append(node.val)
        if not (node.left or node.right):
            if sum(path_nodes) == target:
                paths.append(path_nodes)
        else:
            if node.left:
                find_path(node.left, path_nodes)
            if node.right:
                find_path(node.right, path_nodes)
        path_nodes.pop()

    find_path(root, [])
    return paths
