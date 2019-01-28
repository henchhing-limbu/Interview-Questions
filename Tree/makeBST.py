'''
Input: sorted array
Output: BST
'''


# TODO: Fix this

class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
        
def makeBST(a):
    root = None
    currNode = root
    makeBstHelper(a, root, 0, len(a) -1)
    return currNode

def makeBstHelper(a, node, i, j):
    if i > j:
        return
    mid = (i + j)//2
    node = Node(a[mid])
    makeBstHelper(a, node.left, i, mid -1)
    makeBstHelper(a, node.right, mid + 1, j)


def displayInOrder(root):
    if not root:
        print("No root")
        return
    displayInorder(root.left)
    print(root.val)
    displayInOrder(roo.right)


import random
a= []
for i in range(6):
    a.append(random.randint(1,15))
a.sort()
print(a)
head = makeBST(a)
displayInOrder(head)

    
    
