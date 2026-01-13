class Node:
    def __init__(self, key, val, next, back):
        self.key = key
        self.val = val
        self.next = next
        self.back = back

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.map = {}

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        if node is self.head:
            return node.val
        if node.back:
            node.back.next = node.next
        if node.next:
            node.next.back = node.back
        if node is self.tail:
            self.tail = node.back
        node.back = None
        node.next = self.head
        self.head.back = node
        self.head = node
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.get(key)
            self.map[key].val = value
            return
        if self.size < self.cap:
            node = Node(key, value, self.head, None)
            if self.size == 0:
                self.tail = node
            else:
                self.head.back = node
        else:
            tail_node = self.tail
            del self.map[tail_node.key]
            self.size-=1
            if not tail_node.back:
                self.head = None
                self.tail = None
            else:
                tail_node.back.next = None
                self.tail = tail_node.back
            node = Node(key, value, self.head, None)
            if self.size == 0:
                self.tail = node
            else:
                self.head.back = node
        self.head = node
        self.map[key] = node
        self.size+=1