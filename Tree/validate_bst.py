# given root of a tree
# validate if it is a valid BST

# simply do inorder traversal
# see if the resulting array is sorted
# better if you simple use a variable to track previous max

def isValidBST(root):
	inorder = []
	inOrderHelper(inorder, root)
	for i in range(1, len(inorder)):
		if inorder[i] <= inorder[i-1]:
			return False
	return True	

def inOrderHelper(inorder, node):
	if not node:
		return
	self.inOrderHelper(inorder, node.left)
	inorder.append(node.val)
	self.inOrderHelper(inorder, node.right)

