"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Being a singly linked list, you cannot come from tail towards head.
# So, for this problem, we can simply reverse the second half of the list.
# We can use the technique of slow and fast pointers to reach mid node of the
# list. Then we can simply reverse the second half.
# Now we have two pointers: head and tail.
# We can now simply attaches nodes these pointers are pointing to


def reorder_list(head):
    if not(head and head.next):
        return
    fast_ptr = slow_ptr = head
    while fast_ptr and fast_ptr.next:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
    
    # reverse the second half
    node_ptr = slow_ptr.next
    slow_ptr.next = None
    prev = None
    while node_ptr:
        tmp = node_ptr.next
        node_ptr.next = prev
        prev = node_ptr
        node_ptr = tmp

    # Reorder the list
    head_node = head
    tail_node = prev
    index = 0
    while tail_node:
        if index % 2 == 0:
            tmp = head_node.next
            head_node.next = tail_node
            tail_node = tail_node.next
            head_node = head_node.next
            head_node.next = tmp
        else:
            head_node = head_node.next
        index += 1
