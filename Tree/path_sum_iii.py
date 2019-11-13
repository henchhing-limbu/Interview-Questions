"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# We simply check for every possible parent child path.
# Truly bruteforcing.

def path_sum(root, sum):
    if not root:
        return 0
    return path_sum(root.left, sum) + path_sum(root.right) + _path_sum_helper(
            root, sum)

def _path_sum_helper(root, sum):
    if not root:
        return 0
    num_of_paths = 0
    if root.val == sum:
        num_of_paths += 1
    num_of_paths += _path_sum_helper(
            root.left, sum-root.val) + _path_sum_helper(
                    root.right, sum-root.val)
    return num_of_paths
