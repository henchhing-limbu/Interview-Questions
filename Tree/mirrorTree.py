from binaryTree import BinaryTree, Node, display, inOrder

def mirrorTree(root):
	if not root:
		return root
	newRoot = root
	helper(newRoot)
	return newRoot
	
def helper(node):
	if not node:
		return
	left = node.left
	node.left = node.right
	node.right = left
	helper(node.left)
	helper(node.right)


tree = BinaryTree(5)
tree.insert(3)
tree.insert(4)
tree.insert(6)
tree.insert(7)

display(tree.root)

mirroredTree = mirrorTree(tree.root)
print("Mirrored Tree")
display(mirroredTree)

