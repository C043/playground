from typing import List, Optional
import heapq


# @leet start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        # Seed the heap with the first node from each list (keeping heap size at k).
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, idx, node))

        dummy = ListNode()
        tail = dummy

        while minHeap:
            _, idx, node = heapq.heappop(minHeap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, idx, node.next))

        return dummy.next

    def oNLogNImplementation(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        minHeap = []
        current = None

        # Loop all the linked lists and populate the minHeap
        for list in lists:
            current = list
            while current:
                heapq.heappush(minHeap, current.val)
                if current.next:
                    current = current.next
                else:
                    current = None

        if not minHeap:
            return

        firstNode = ListNode(heapq.heappop(minHeap), None)
        currentNode = firstNode

        # While len(minHeap) > 0 pop from the heap and create the linked list to return
        while len(minHeap) > 0:
            currentNode.next = ListNode(heapq.heappop(minHeap))
            currentNode = currentNode.next

        return firstNode


# @leet end
linkedList = ListNode(1, ListNode(4, ListNode(5)))
linkedList2 = ListNode(1, ListNode(3, ListNode(4)))
linkedList3 = ListNode(2, ListNode(6))

solution = Solution()
print(solution.mergeKLists([linkedList, linkedList2, linkedList3]))

"""
This implementation is O(n log k) time complexity because each of the n nodes is pushed/popped from a heap of size k.
This implementation is O(k) space complexity because the heap stores at most one node per list.

The implementation is fairly simple:
- We push the head node from each list into the min heap (keeping it size k).
- We repeatedly pop the smallest node, append it to the result, and push that node's successor into the heap.
"""
