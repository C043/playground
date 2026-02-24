from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.dfs(root) != -1

    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left = self.dfs(node.left)
        if left == -1:
            return -1
        right = self.dfs(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
root = TreeNode(
    1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2)
)
solution = Solution()
print(solution.isBalanced(root))
