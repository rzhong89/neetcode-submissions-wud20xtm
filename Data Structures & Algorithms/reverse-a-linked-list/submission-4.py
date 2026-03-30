# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Ok, so what I'm thinking is we need a previous 
        # pointer so that when we reattach it backwards, 
        # we want the current to attach to previous. 
        # Then, since we reattach it, we also need a temporary
        # pointer that has the next thing. 

        prev = None
        current = head
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            

        return prev