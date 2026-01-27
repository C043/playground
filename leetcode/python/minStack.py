from typing import List


class MinStack:

    def __init__(self):
        self.stack: List[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # Brute force implementation
        return min(self.stack)


# O(1) implementation
class MinStack:

    def __init__(self):
        self.stack: List[int] = []
        self.minStack: List[int] = []
        self.currentMin: int | None = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


"""
This implementation is fairly simple.
The main idea is to keep a list beside the main stack list in which we always append the minimum between the new value and the current min value. This way, when we pop, we pop from both stacks to keep them aligned. The self.minStack will always have the minimum value from the main stack as its last element.
When we want to check the min value in the stack, we just need to look at the last element in the min list we're keeping.

This implementation is O(1) time complexity for all the operations.
This implementation is O(n) space complexity because even if it stores data two times, once for the self.stack list and once for the self.minStack list, the space grows linearly with the input growth.
"""
