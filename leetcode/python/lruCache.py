from typing import Dict


class Node:
    def __init__(self, key, val):
        self.key: int | None = key
        self.val: int | None = val
        self.next: Node | None = None
        self.prev: Node | None = None


class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(None, None)
        self.tail = Node(None, None)
        # These are important as they are sentinels: head and tail will always be dummy nodes
        self.tail.prev = self.head
        self.head.next = self.tail

    def add(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
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
            popped = self.tail.prev
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            self.size = self.size - 1
            return popped.key


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
            node = Node(key, value)
            node = self.dll.add(node)
            self.map[key] = node

        if self.dll.size > self.capacity:
            keyToRemove = self.dll.pop()
            del self.map[keyToRemove]


cache = LRUCache(2)
cache.put(1, 2)
cache.put(3, 5)
cache.put(6, 9)
print(cache.get(1))
print(cache.dll.head.next.val)
print(cache.dll.tail.prev.val)
print("----")
print(cache.dll.size)

"""
The main idea behind this implementation is to combine a hashmap and a doubly linked list in order to have fast access to the data we need and sort it in the fastest way possible.
We need to sort data because the LRUCache has a capacity.
If we try to add data beyond that capacity, we must evict the least used key. This means that we need to track the most and least used keys.
The map is key = int, value = doubly linked list node.
When we get by key, we return the node value if we have it in the map otherwise we return -1.
But if we have the node, we also need to put that node at the top of the doubly linked list.

When we put with key and value, we first check if we already have that key in the map.
If we have it, we put it at the top of the doubly linked list with the new value.
Otherwise we just create a new node and add it to the top of the doubly linked list.
In both cases we obviously add the node to the map as well.
Then if the size of the doubly linked list is more than the LRUCache capacity, we pop the last node of the doubly linked list and delete its key from the map.

The time complexity of get and put methods is O(1) constant time because we have fast access to the all the nodes we need thanks to the combination of the map and the doubly linked list.

The space complexity of this all algorithm is O(n) where n is the LRUCache capacity.
"""
