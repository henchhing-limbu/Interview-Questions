class Node:
	def __init__(self, data = None, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right
	

def create_bst(a):
	root = Node()
	helper(a, root, 0, len(a))
	return root

def helper(a, node, i, j):
	if i >=  j:
		return

	mid = (i + j)//2
	node.data = a[mid]
	node.left = Node()
	node.right = Node()
	
	helper(a, node.left, i, mid)
	helper(a, node.right, mid+1, j)

def inorder_traversal(root):
	if not root:
		return
	inorder_traversal(root.left)
	print(root.data)
	inorder_traversal(root.right)

node = create_bst([1,2,3,4,5,6,7])
inorder_traversal(node)

