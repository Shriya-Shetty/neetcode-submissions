# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            # Step 1: check if there are k nodes ahead
            node = prev
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next

            # Step 2: reverse k nodes
            curr = prev.next
            nxt = curr.next
            for _ in range(k - 1):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next

            # Step 3: move prev forward for next group
            prev = curr
