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
        current = None

        # Loop all the linked lists and populate the minHeap
        for list in lists:
            current = list
            while current:
                print(current.val)
                heapq.heappush(minHeap, current.val)
                if current.next:
                    current = current.next
                else:
                    current = None

        print(minHeap)
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
