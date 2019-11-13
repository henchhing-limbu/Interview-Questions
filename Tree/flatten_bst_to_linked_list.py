"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

def flatten(root):
    stack = []
    while root:
        if root.right:  # The right child needs to be added after the left
                        # subtree is dealt with.
                stack.append(root.right)

        if root.left:	# if there is right child
                root.right = root.left
        elif stack:	# get the node from the stack
                root.right = stack.pop()
        # Left subtree is already moved to be right subtree. So, make the left
        # subtree to be None, and make root to be right child.
        root.left = None
        root = root.right
