"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Using post order, we can find the root of the tree.
# [9, 15, 7, 20, (3)]
# Using the root of the tree, we can find the length of right and left subtree
# from the inorder. 
# [9, (3), 15, 20, 7]
# Then, we can use the same logice above to find root of the subtrees and so on
# until we finish building the tree.

def build_tree(inorder, postorder):
    if not postorder:
        return None
    root_val = postorder.pop()
    root = TreeNode(root_val)
    partition_idx = inorder.index(root_val)
    root.left = build_tree(inorder[:partition_idx], postorder[:partition_idx])
    root.right = build_tree(inorder[partition_idx+1:], postorder[partition_idx:])
    return root
