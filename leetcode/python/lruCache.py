from typing import Dict


class Node:
    def __init__(self, val):
        self.val = val
        self.next: Node
        self.prev: Node


class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(0)
        self.tail = self.head
        self.head.prev = self.tail
        self.tail.next = self.head

    def add(self, node: Node):
        current = node
        self.head.next = current
        current.prev = self.head
        self.head = current
        self.size = self.size + 1
        return self.head

    def remove(self, node: Node):
        next = node.next
        prev = node.prev
        next.prev = prev
        prev.next = next
        return node

    def pop(self):
        if self.size == 0:
            return -1
        else:
            current = self.tail
            self.tail = self.tail.next
            self.tail.prev = Node(0)
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
            self.dll.remove(item)
            node = Node(value)
            node = self.dll.add(node)
            self.map[key] = node
        else:
            node = Node(value)
            node = self.dll.add(node)
            self.map[key] = node
            if self.dll.size > self.capacity:
                self.dll.pop()
