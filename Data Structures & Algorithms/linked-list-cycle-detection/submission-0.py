# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        list1=[]
        while curr not in list1:
            if curr is None:
                return False
            list1.append(curr)
            curr=curr.next
        return True
            
        