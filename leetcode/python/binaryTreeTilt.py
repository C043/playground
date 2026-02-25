from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.total += abs(left - right)
            return node.val + left + right

        dfs(root)
        return self.total


root = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
print(solution.findTilt(root))
