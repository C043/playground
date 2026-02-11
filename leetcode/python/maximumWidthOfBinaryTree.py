from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 0)])
        maxWidth = 0

        while queue:
            level = queue.copy()
            maxWidth = max(maxWidth, level[-1][1] - level[0][1] + 1)
            for i in range(len(level)):
                node, index = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))

        return maxWidth


root = TreeNode(
    1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9))
)
solution = Solution()
print(solution.widthOfBinaryTree(root))

"""
This solution uses BFS combined with a index system to calculate the width of every level.
All left nodes are given 0 index and all right nodes are given 2 * the index of its parent + 1.
This makes the right index grow exponentially.
We calculate the current width by using this formula:
- last node index of the queue - first index of the queue plus one

Once we have an entire level, we can calculate its width.
With the width we can keep a max value that we return in the end.

The time complexity is O(n) because we visit every node
The space complexity is O(w) where w is the max width of the tree
"""
