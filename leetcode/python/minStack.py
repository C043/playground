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
