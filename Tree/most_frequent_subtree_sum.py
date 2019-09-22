"""
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""

def find_frequent_tree_sum(root):
	tree_sum_dict = {}
	_find_tree_sum(root, tree_sum_dict)

	max_count_values = []
	max_count = 0
	for key, val in tree_sum_dict.items():
		if val > max_count:
			max_count_vales = [key]
			max_count = val
		elif val == max_count:
			max_count_values.append(key)
	return max_count_values


def _find_tree_sum(node, tree_sum_dict):
	if node is None:
		return 0
	subtree_sum = helper(node.left, tree_sum_dict) + helper(node.right, tree_sum_dict) + node.val
	if subtree_sum in tree_sum_dict:
		tree_sum_dict[subtree_sum] += 1
	else:
		tree_sum_dict[subtree_sum] = 1
	return subtree_sum
