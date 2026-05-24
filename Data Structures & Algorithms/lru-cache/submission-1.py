class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove from cache
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    
    def remove(self, node):
        nxt = node.next
        node.prev.next = nxt
        nxt.prev = node.prev

    def insert(self, node):
        last = self.right.prev
        last.next = node
        node.prev = last
        node.next = self.right
        self.right.prev = node
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
