# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # So what I'm thinking is we'll have two current pointers, 
        # curr1 and curr2, and then we compare them with each other 
        # in a while loop. Put one first based on the comparison,
        #  and then move that pointer forward, and then compare it 
        #  again, and then move it forward, based on which one. At 
        #  the end, we might have a list left over, and then we'll 
        #  just attach that at the end. 

        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        elif list2:
            node.next = list2

        return dummy.next
