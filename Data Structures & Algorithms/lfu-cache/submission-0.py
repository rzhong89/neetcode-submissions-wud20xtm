class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = self.prev = None

class DoublyLinkedList:
    """Most recent at head, least recent at tail"""
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_map = {}            # key → node
        self.freq_map = {}           # freq → DLL

    def _increment_freq(self, node):
        f = node.freq
        self.freq_map[f].remove(node)
        if self.freq_map[f].size == 0 and f == self.min_freq:
            self.min_freq += 1
        node.freq += 1
        self.freq_map.setdefault(node.freq, DoublyLinkedList())
        self.freq_map[node.freq].add_to_front(node)

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        node = self.key_map[key]
        self._increment_freq(node)
        return node.value           # return value, not key

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_map:
            self.key_map[key].value = value
            self._increment_freq(self.key_map[key])
        else:
            if len(self.key_map) >= self.capacity:
                evicted = self.freq_map[self.min_freq].remove_last()
                del self.key_map[evicted.key]
            node = ListNode(key, value)
            self.key_map[key] = node
            self.freq_map.setdefault(1, DoublyLinkedList())
            self.freq_map[1].add_to_front(node)
            self.min_freq = 1       # new node always resets min_freq to 1