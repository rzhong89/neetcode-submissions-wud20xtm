# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # So what I'm thinking is we just have a slow pointer
        #  and a fast pointer, and the slow pointer moves one pace
        #   and then the fast pointer moves two at a time until 
        # the fast pointer stops
        #   I'm thinking that eventually, if there's a cycle, 
        #   then the pointers will meet up again. 

        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False