from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result: List[int] = []

        queue: deque[TreeNode] = deque([root])

        while len(queue) > 0:
            level = queue

            for i in range(len(level)):
                node = queue.popleft()
                if i == 0:
                    result.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return result


root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))
solution = Solution()
print(solution.rightSideView(root))

"""
This implementation uses a BFS in order to traverse each level of the tree. At every level, we enque the right node first so we'll know that at the start of every level, the first node of the level will be the rightmost one. We append the value of that node to the result list we return at the end. We do this for every level.

Time complexity is O(n) because we visit each node once
Space complexity is O(w) where w is the max width of the tree
"""
