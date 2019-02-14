class Node:
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class BinaryTree:
	def __init__(self, val):
		self.root = Node(val)
	
	def insert(self, val):
		if not self.root:
			self.root = Node(val)
		else:
			self.insertHelper(self.root, val)

	def insertHelper(self, node, val):
		if node.val > val:
			if not node.left:
				node.left = Node(val)
			else:
				self.insertHelper(node.left, val)
		else:
			if not node.right:
				node.right = Node(val)
			else:
				self.insertHelper(node.right, val)

def display(root):
	inOrder(root)
	
def inOrder(node):
	if not node:
		return
	inOrder(node.left)
	print(node.val)
	inOrder(node.right)
