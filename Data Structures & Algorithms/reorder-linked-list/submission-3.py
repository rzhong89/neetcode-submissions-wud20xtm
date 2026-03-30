# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
We can just have a slow and fast pointer so that when the fast 
pointer reaches the end of the linked list, the slow pointer will 
be in the middle. From there, we can reverse the second part of 
the list, and then we just start zipping it. Take the first element 
of the first list, and then the second element; take that and then 
the first element of the second list, and keep going. 
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half of list
        prev = None
        second = slow.next
        slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        
        # zip it up
        curr = head
        while curr and prev:
            temp = curr.next
            curr.next = prev
            temp1 = prev.next
            prev.next = temp
            curr = temp
            prev = temp1




        
        



        

        


