'''
I think for this problem to have get and put each run in O1 average 
time complexity, we're going to need to use two data structures.
- For get, I'm thinking we should use a hash map so that the key 
maps to its value. It would just be an O1 function call.
- For put, I think since we need the least recently used key, we 
can use something like a linked list. Every time we put something 
in, we will update it so it goes out the front, so it is the most 
recently used. The least recently used is at the end of the list, 
and then we can just remove that.
'''

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        #hashmap of key: listNode
        #Listnode of next, prev, key, value
        #capactiy 
        self.map = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.add(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        # check if new
        # add to front of linkedlist
        # check capactiy: remove

        if key in self.map:
            node = self.map[key]
            node.value = value
            self.remove(node)
            self.add(node)
        else: # add to linkedlist and map
            node = ListNode(key, value)
            self.map[key] = node
            self.add(node)

        if len(self.map) > self.capacity:
            del self.map[self.tail.prev.key]
            self.remove(self.tail.prev)

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add(self, node):
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node

