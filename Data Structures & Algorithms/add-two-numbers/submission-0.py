# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)   # starting dummy node
        tail = dummy          # tail builds the result
        curr1, curr2 = l1, l2
        carry = 0

        # loop until both lists are exhausted
        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # create new node for this digit
            tail.next = ListNode(digit)
            tail = tail.next

            # move forward
            if curr1: 
                curr1 = curr1.next
            if curr2: 
                curr2 = curr2.next

        return dummy.next   # skip dummy, return head of result
