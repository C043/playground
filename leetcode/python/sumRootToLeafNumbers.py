from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root and not root.left and not root.right:
            return root.val

        return self.traverse(root.left, root.val) + self.traverse(root.right, root.val)

    def traverse(self, root: Optional[TreeNode], compiledNum: int) -> int:
        if not root:
            return 0
        if root and not root.left and not root.right:
            return int(str(compiledNum) + str(root.val))

        compiledNum = int(str(compiledNum) + str(root.val))

        return self.traverse(root.left, compiledNum) + self.traverse(
            root.right, compiledNum
        )


root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
root = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
print(solution.sumNumbers(root))
