# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Copy each node and insert it right after the original
        curr = head
        while curr:
            newNode = Node(curr.val)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next

        # Step 2: Assign random pointers for the copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the two lists
        curr = head
        newhead = head.next
        newcurr = newhead
        while curr:
            curr.next = curr.next.next
            if newcurr.next:
                newcurr.next = newcurr.next.next
            curr = curr.next
            newcurr = newcurr.next

        return newhead
