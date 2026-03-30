"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        ogToCopy = {None: None}


        while current:
            node = Node(current.val)
            ogToCopy[current] = node
            current = current.next

        current = head

        while current:
            copy = ogToCopy[current]
            copy.next = ogToCopy[current.next]
            copy.random = ogToCopy[current.random]
            current = current.next
        
        return ogToCopy[head]
            