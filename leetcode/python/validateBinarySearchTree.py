from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return True


root = TreeNode(5, TreeNode(1, TreeNode(4, TreeNode(3), TreeNode(6))))
root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
root = TreeNode(2, TreeNode(1), TreeNode(3))
root = TreeNode(2, TreeNode(2), TreeNode(2))
root = TreeNode(45, TreeNode(42, None, TreeNode(44, TreeNode(43, TreeNode(41)))))
solution = Solution()
print(solution.isValidBST(root))
