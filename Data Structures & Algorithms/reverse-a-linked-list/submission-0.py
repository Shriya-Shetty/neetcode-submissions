# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            # Save next node
            nxt = curr.next
            # Reverse pointer
            curr.next = prev
            # Move prev and curr forward
            prev = curr
            curr = nxt

        return prev   # new head
