def isHeightBalancedBst(node):
    '''
    base case return 0 if the node is node is none
    for every recursive call add 1
    check if the absolute difference of right subtree and left subtree is more than 1
    '''
    if not node:
        return 0
    leftDepth = isHeightBalancedBst(node.left)
    rightDepth = isHeightBalancedBst(node.right)

    if leftDepth == -1 or rightDepth == -1:
        return -1
    if abs(leftDepth - rightDepth) > 1:
        return -1
    return max(leftDepthk, rightDepth) + 1

    
