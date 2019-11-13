"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# This is simply level order traversal type question.
# Just save the rightmost node value of each level.

def right_side_view(root):
    if not root:
        return []

    result = []
    curr_lvl_nodes = [root] # holds current tree level nodes
    while curr_lvl_nodes:
        next_lvl_nodes = [] # holds next tree level nodes
        result.append(curr_lvl_nodes[-1].val)
        for node in curr_lvl_nodes:
            if node.left:
                next_lvl_nodes.append(node.left)
            if node.right:
                next_lvl_nodes.append(node.right)
        # next level nodes needs to be current level nodes for next iteration.
        curr_lvl_nodes = next_lvl_nodes
    return result
