from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels: List[List[int]] = []
        queue: deque[TreeNode] = deque([root])

        while queue:
            level = len(queue)
            currentLevel: List[int] = []

            for i in range(level):
                node = queue.popleft()
                currentLevel.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(currentLevel)

        return levels


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
solution = Solution()
print(solution.levelOrder(root))

"""
This solutions uses basic BFS traversal to traverse the tree.
It tracks the current level values and at the end of the level, it adds those values in a list to return in the end.
When we traverse all the tree, we return that list.

The time complexity is O(n) because we traverse all the nodes of the tree once
The space complexity is O(w) as we keep track at most of the max width of the tree
"""
