'''
method to find minimum depth of a binary tree
'''
from collections import deque
def findMinDepth(node):
    q = deque()
    q.append([node])
    depth = 0
    while q:
        newNodes = []
        nodes = q.pop()
        for x in nodes:
            if not x:
                return depth
            newNodes.append(x.left)
            newNodes.append(x.right)
        depth += 1
        if newNodes:
            q.append(newNodes)
    return depth
        


    
