from typing import Set, Dict


class Node:
    __slots__ = ("cnt", "keys", "prev", "next")

    def __init__(self, cnt: int):
        self.cnt: int = cnt
        self.keys: Set[str] = set()
        self.prev: "Node" | None = None
        self.next: "Node" | None = None


class AllOne:
    def __init__(self):
        # Sentinels: head <-> ...buckets... <-> tail
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        # key -> bucket node
        self.loc: Dict[str, Node] = {}

    def _insert_after(self, node: Node, new_node: Node) -> None:
        nxt = node.next
        new_node.prev = node
        new_node.next = nxt
        node.next = new_node
        if nxt:
            nxt.prev = new_node

    def _remove_node(self, node: Node) -> None:
        prv, nxt = node.prev, node.next
        if prv:
            prv.next = nxt
        if nxt:
            nxt.prev = prv
        node.prev = node.next = None  # help GC

    def inc(self, key: str) -> None:
        if key not in self.loc:
            # treat as coming from head (count 0)
            curr = self.head
            next_bucket = curr.next
            if next_bucket is self.tail or next_bucket.cnt != 1:
                nb = Node(1)
                self._insert_after(curr, nb)
                next_bucket = nb
            next_bucket.keys.add(key)
            self.loc[key] = next_bucket
            return

        curr = self.loc[key]
        target_cnt = curr.cnt + 1
        nxt = curr.next
        if nxt is self.tail or nxt.cnt != target_cnt:
            nb = Node(target_cnt)
            self._insert_after(curr, nb)
            nxt = nb

        # move key
        curr.keys.remove(key)
        nxt.keys.add(key)
        self.loc[key] = nxt

        # delete empty bucket
        if not curr.keys:
            self._remove_node(curr)

    def dec(self, key: str) -> None:
        curr = self.loc[key]
        target_cnt = curr.cnt - 1

        # remove key from current bucket first
        curr.keys.remove(key)

        if target_cnt == 0:
            # key removed entirely
            del self.loc[key]
        else:
            prv = curr.prev
            if prv is self.head or prv.cnt != target_cnt:
                nb = Node(target_cnt)
                self._insert_after(curr.prev, nb)  # insert before curr
                prv = nb
            prv.keys.add(key)
            self.loc[key] = prv

        # delete empty bucket
        if not curr.keys:
            self._remove_node(curr)

    def getMaxKey(self) -> str:
        node = self.tail.prev
        if node is self.head:
            return ""
        return next(iter(node.keys))

    def getMinKey(self) -> str:
        node = self.head.next
        if node is self.tail:
            return ""
        return next(iter(node.keys))