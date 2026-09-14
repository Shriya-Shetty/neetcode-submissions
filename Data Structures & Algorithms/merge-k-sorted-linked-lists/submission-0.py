# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []

        # Step 1: collect all values into a list
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next

        # Step 2: sort the list
        values.sort()

        # Step 3: build new linked list
        dummy = ListNode(0)
        curr = dummy
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
