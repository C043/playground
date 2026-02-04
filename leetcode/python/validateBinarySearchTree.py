from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(
        self,
        root: Optional[TreeNode],
    ) -> bool:
        if not root:
            return True

        return self.check(root, float("-inf"), float("inf"))

    def check(self, root: Optional[TreeNode], low: float, high: float) -> bool:
        if not root:
            return True
        if not (low < root.val < high):
            return False
        return self.check(root.left, low, root.val) and self.check(
            root.right, root.val, high
        )


root = TreeNode(45, TreeNode(42, None, TreeNode(44, TreeNode(43, TreeNode(41)))))
root = TreeNode(2, TreeNode(2), TreeNode(2))
root = TreeNode(2, TreeNode(1), TreeNode(3))
root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
root = TreeNode(
    3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(6))
)
solution = Solution()
print(solution.isValidBST(root))
