from typing import List, Optional
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        best = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1

            best = max(best, dfs(node.left), dfs(node.right) + 2)
            return max(dfs(node.left), dfs(node.right)) + 1

        dfs(root)
        return best


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
solution = Solution()
print(solution.diameterOfBinaryTree(root))
