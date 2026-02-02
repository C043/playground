from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        elif not root.left and root.right or not root.right and root.left:
            return False

        return self.check(root.left, root.right)

    def check(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        elif not left and right or not right and left:
            return False
        elif right and left and right.val != left.val:
            return False

        leftTraversal = False
        rightTraversal = False
        if left and left.left and right and right.right:
            leftTraversal = self.check(left.left, right.right)
        if left and left.right and right and right.left:
            rightTraversal = self.check(left.right, right.left)

        return leftTraversal or rightTraversal


root = TreeNode(
    5,
    TreeNode(2, TreeNode(4, None, TreeNode(1))),
    TreeNode(2, None, TreeNode(1, TreeNode(2))),
)
root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
root = TreeNode(
    1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))
)
solution = Solution()
print(solution.isSymmetric(root))
