class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.listMap = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.listMap:
            node = self.listMap[key]
            self.delete(node)
            self.moveToFront(node)
            return self.listMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.listMap:
            # update
            self.listMap[key].val = value
            # move to front
            node = self.listMap[key]
            self.delete(node)
            self.moveToFront(node)
        else:
            # add to hashMap
            # add to front of list
            newNode = ListNode(key, value)
            self.listMap[key] = newNode
            self.moveToFront(newNode)

            if len(self.listMap) > self.capacity:
                deleteNode = self.tail.prev
                self.delete(deleteNode)
                del self.listMap[deleteNode.key]
            

    def moveToFront(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        
        node.prev = self.head
        temp.prev = node

    def delete(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev