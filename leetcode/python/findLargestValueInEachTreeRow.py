from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue: deque[TreeNode] = deque([root])
        result: List[int] = []

        while queue:
            level = len(queue)
            maxValue = float("-inf")
            for i in range(level):
                node = queue.popleft()

                maxValue = max(maxValue, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(int(maxValue))

        return result


root = TreeNode(
    1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9))
)

root = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
print(solution.largestValues(root))

"""
This solution uses BFS traversal in order to keep track of the max value of each level and at the end of the for loop, when we cycled all the current level, we append the max value to the list we'll return.

The time complexity is O(n) because we visit every node once
The space complexity is O(w) where w is the max width of the tree because we store one level at a time in the queue
"""
