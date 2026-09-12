# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Store nodes in list1
        list1 = []
        curr = head
        while curr:
            list1.append(curr)
            curr = curr.next

        # Step 2: Reorder using two pointers
        i, j = 0, len(list1) - 1
        while i < j:
            list1[i].next = list1[j]
            i += 1
            if i == j:
                break
            list1[j].next = list1[i]
            j -= 1

        # Step 3: End the list
        list1[i].next = None
