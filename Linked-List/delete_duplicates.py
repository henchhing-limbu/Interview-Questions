"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

Input: 1->2->3->3
Output: 1->2
"""

def delete_duplicates(head):
    curr_node = head
    dummy_ptr = prev_node = ListNode(None)
    while curr_node:
        dup_node = curr_node.next
        # Find next node whose value is not identical to curr node's value
        while dup_node and dup_node.val == curr_node.val:
            dup_node = dup_node.next
        if dup_node is None or dup_node != curr_node.next:
            prev_node.next = dup_node
        curr_node = dup_node
    return dummy_ptr.next
