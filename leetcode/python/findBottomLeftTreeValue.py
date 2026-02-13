from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue: deque[TreeNode] = deque([root])
        result = 0

        while queue:
            level = len(queue)

            for i in range(level):
                node = queue.popleft()

                if i == 0:
                    result = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5, TreeNode(6))))
solution = Solution()
print(solution.findBottomLeftValue(root))

"""
This implementation uses BFS traversal and tracks the leftmost value at each level.
At the end of traversal, we return the variable.

Time complexity is O(n) because we visit each node once
Space complexity is O(w) because we store in the queue at most the max width of the tree
"""
