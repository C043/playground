from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Get the two numbers as digits in two lists
        firstNum = self.getListByLinkedList(l1)
        secondNum = self.getListByLinkedList(l2)

        # Reverse them
        firstNum.reverse()
        secondNum.reverse()

        # Join them
        firstNum = int("".join(map(str, firstNum)))
        secondNum = int("".join(map(str, secondNum)))

        # Sum them
        result = firstNum + secondNum

        # Split the number in an array
        resultList = [int(ch) for ch in str(result)]

        # Reverse the number
        resultList.reverse()

        # Convert it to a linked list and return it
        listLinkToReturn = self.getLinkedListByList(resultList)

        return listLinkToReturn

    def getListByLinkedList(self, node: Optional[ListNode]) -> List[int]:
        listToReturn: List[int] = []
        cur = node
        while cur is not None:
            listToReturn.append(cur.val)
            cur = cur.next

        return listToReturn

    def getLinkedListByList(self, nums: List[int]) -> Optional[ListNode]:
        if not nums:
            return None
        return ListNode(nums[0], self.getLinkedListByList(nums[1:]))

    def addTwoNumbersOptimized(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


solution = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

head = solution.addTwoNumbersOptimized(l1, l2)
print(head.val)
print(head.next.val)
print(head.next.next.val)

"""
Here I implemented two ways of solving this:
The unoptimized way converts the linked list to a list.
It reverses it and join it parsing the int (which can be very expensive).
Sums the two numbers.
Split the total, reverses it and converts it to a linked list again returning its head.

The optimized implementation does not convert anything. It's much simpler:
The main idea behind it is that we loop over all the nodes in the linked lists.
We sum the values of the current nodes plus the carry.
We calculate the carry based on the sum total and create a list node with the last digit of the total. This way we have both digits if the number is greater than 9.
We keep going until we looped over all the nodes in both linked lists.
We then return the first node of the linked list (bypassing the dummy we created earlier).

The optimized implementation is O(n) time complexity as it grows linearly with the length of the two linked lists. (There is just one loop).
The space complexity of the optimized implementation is O(1) excluding the output. We just keep some variables in memory.

The time complexity of the unoptimized implementation is O(n) as it saves a lot of lists, strings, big ints that grow linearly with the total number of nodes in the linked lists.
"""
