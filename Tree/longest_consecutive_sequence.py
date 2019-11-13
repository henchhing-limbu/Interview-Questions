"""
Give a binary tree, find the length of longest consecutive sequence path.
The path refers to any sequence of nodes from some starting node to any node
in the tree along the parent child connections. The longest consecutive path
need to be from parent to child (cannot be reverse).
"""

def longest_conseutive_sequence_path_length(root):
    if not root:
        return 0

    max_length = 0
    # Stack stores a tuple where the elements are tuples.
    # The format of each tuple is:
    #   0 - node
    #   1 - length of longest subsequence with current node
    stack = [(root, 1)]
    while stack:
        node_info = stack.pop()
        node = node_info[0]
        max_length = max(
                max_length, helper(node.left, stack, node_info),
                helper(node.right, stack, node_info))
    return max_length

def helper(child_node, stack, node_info):
    if not child_node:
        return node_info[1]

    # Return length of longest subsequence with child node value as end.
    if child_node.val-1 == node_info[0].val:
        stack.append((child_node, node_info[0]+1))
        return node_info[0]+1
    else:
        stack.append((child_node, 1))
        return 1
