"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""

# This is just a variation of level order traversal.
# As long as you have nodes of each level, you can simply make a node's next
# point to neighboring node.

def connect(root):
	if root is None:
		return root
	lvl_nodes = [root]
	while lvl_nodes:
		nxt_lvl_nodes = []
		for i in range(len(lvl_nodes)):
			if i == len(lvl_nodes)-1:
				lvl_nodes[i].next = None
			else:
				lvl_nodes[i].next = lvl_nodes[i+1]
			
			if lvl_nodes[i].left:
				nxt_lvl_nodes.append(lvl_nodes[i].left)
			if lvl_nodes[i].right:
				nxt_lvl_nodes.append(lvl_nodes[i].right)
		lvl_nodes = nxt_lvl_nodes
	return root
