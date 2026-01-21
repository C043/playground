from typing import Dict


class Node:
    def __init__(self, val):
        self.val: int | None = val
        self.next: Node | None = None
        self.prev: Node | None = None


class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.tail.prev = self.head
        self.head.next = self.tail

    def add(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.prev = Node(None)
        self.head.next = node
        self.size = self.size + 1
        return self.head.next

    def remove(self, node: Node):
        if node.next != None and node.prev != None:
            next = node.next
            prev = node.prev
            prev.next = next
            next.prev = prev
            self.size = self.size - 1
        return node

    def pop(self):
        if self.size == 0:
            return
        else:
            current = self.tail
            self.tail = self.tail.prev
            self.tail.next = self.tail.next
            self.size = self.size - 1
            return current


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: Dict[int, Node] = dict()
        self.dll: DoublyLinkedList = DoublyLinkedList()

    def get(self, key: int) -> int:
        item = self.map.get(key)
        if item:
            node: Node = self.dll.remove(item)
            self.dll.add(node)
            return item.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        item = self.map.get(key)
        if item:
            node = self.dll.remove(item)
            node.val = value
            node = self.dll.add(node)
            self.map[key] = node
        else:
            node = Node(value)
            node = self.dll.add(node)
            self.map[key] = node

        if self.dll.size > self.capacity:
            self.dll.pop()
            del self.map[key]


cache = LRUCache(2)
cache.put(1, 2)
cache.put(3, 5)
cache.put(6, 9)
print(cache.get(1))
print(cache.dll.head.next.val)
print(cache.dll.tail.prev.val)
print("----")
print(cache.dll.size)
