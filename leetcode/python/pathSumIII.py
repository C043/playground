from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        if targetSum - root.val == 0:
            return 1

        return

    def helper(
        self, root: Optional[TreeNode], targetSum: int, path: deque[int], count: int
    ) -> int:
        if not root:
            return count


root = TreeNode(
    5,
    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
    TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))),
)
root = TreeNode(
    10,
    TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))),
    TreeNode(-3, None, TreeNode(11)),
)
solution = Solution()
print(solution.pathSum(root, 8))
#        5
#      /   \
#     4     8
#    /     / \
#   11    13  4
#  / \       / \
# 7   2     5   1
