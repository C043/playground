from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root and not root.left and not root.right and targetSum - root.val == 0:
            return True

        left = False
        right = False

        if root and root.left:
            left = self.hasPathSum(root.left, targetSum - root.val)
        if root and root.right:
            right = self.hasPathSum(root.right, targetSum - root.val)

        return left or right


root = TreeNode(
    5,
    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
    TreeNode(
        8,
        TreeNode(13),
        TreeNode(4, None, TreeNode(1)),
    ),
)

root = TreeNode(-2, None, TreeNode(-3))
solution = Solution()
print(solution.hasPathSum(root, -5))
