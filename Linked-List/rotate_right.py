"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

# Indexing can't be done in linked list.
# Being a singly linked list, you can't iterate from tail of the list.

# One way to do this would be to reverse the list. Then, iterate until k nodes
# in the reversed list. Then make curr node next head of the new list and make
# the end of the list point to current head of the list. 

# The above approach requires reversing the list. Something better than that
# would be to move two pointers separated by k nodes. When the front pointer
# reaches end of the list, the back pointer reachs k node from behing of the
# list.


def rotate_right(root, k):
    if root is None:
        return root
    # find the size of the list
    l_size = 0
    node = root
    while node:
        l_size += 1
        node = node.next

    # take modulo to find how many nodes to move forward from head.
    k = k%size
    if k == 0:
        return root

    # Move the forward pointer by k nodes
    forward_ptr = root
    for _ in range(k):
        forward_ptr = forward_ptr.next

    # move forward and back pointers until forward pointer is last node.
    back_ptr = root
    while forward_ptr.next:
        back_ptr = back_ptr.next
        forward_ptr = forward_ptr.next
    # Split the list and reattach them as instructed.
    head = back_ptr.next
    back_ptr.next = None
    forward_ptr.next = root
    return head
