from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return
        queue: deque[Node] = deque([root])
        current = None

        while queue:
            level = len(queue)

            for i in range(level):
                node = queue.popleft()

                if current:
                    current.next = node

                current = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            current = None

        return root


root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
solution = Solution()
print(solution.connect(root))

"""
This implementation uses BFS traversal and keep a variable called "current" outside of the loops.
As we progress through the traversal, we assign the current property next to the current node we're visiting.
Then at the end of every level, we reset the "current" variable to None.

The time complexity is O(n) because we visit every node once
The space complexity is O(w) where w = max width of the tree, in this case it's the level where the leaves are
"""
