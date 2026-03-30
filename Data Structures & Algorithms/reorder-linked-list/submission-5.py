# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        beforeMiddle = head
        fast = head

        while fast.next and fast.next.next:
            beforeMiddle = beforeMiddle.next
            fast = fast.next.next
        
        secondList = beforeMiddle.next

        #disconnect lists
        beforeMiddle.next = None

        # reverse 2nd list
        prev = None
        while secondList:
            temp = secondList.next
            secondList.next = prev
            prev = secondList
            secondList = temp
        
        # now zip first list and prev up
        # first list will always be bigger
        curr = head

        while curr and prev:
            temp = curr.next
            curr.next = prev
            temp1 = prev.next
            curr = temp
            prev.next = curr
            prev = temp1

        
        