"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

# If you haven't used two-pointers before, then the first thing that comes to
# your mind is to go through the list once and find it's length. After then,
# you can simply iterate until list.size - n and return that node.
# However, this requires two pass.

# Using two pointers (or simple algebra) we can do this one pass. We will
# use two pointers that maintain a distanc of n. Each unit of distance is
# a node here. The two pointers point to two nodes; let's call them slow
# and fast pointer. We first move fast pointer to nth position from start.
# Then, we make slow pointer point to start and move both pointers 
# simulatneously. When the fast pointer reaches the end, the slow pointer
# will be in nth poisition from end. Don't believe? Try to draw it out.
# Everything will make sense :)

# We will make use of dummy pointer to keep track of head. This can be very
# useful thing sometimes.

def remove_nth_from_end(head, n):
    dummy_ptr = ListNode(None)
    dummy_ptr.next = head
    fast_ptr = slow_ptr = dummy_ptr
    for i in range(1, n+2):
        fast_ptr = fast_ptr.next
    while fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    slow_ptr.next = slow_ptr.next.next
    return dummy_ptr.next
    
