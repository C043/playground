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

"""
This implementation uses DFS to find the leaves and see if the target sum is 0 after subtracting the root value.
It is recursive. We call the method on root left and on root right with passing the root left and root right and the target sum minus the current root value.
We assign the result of these recursive calls to two boolean variables and we return true if any one of these is true. Otherwise we return false.
The recursive base case is that the node is a leaf and that target sum is 0 after subtructing the current node value.

The time complexity is O(n) because we visit each node exactly once
The space complexity is O(1) if we're not counting the call stack
If we're counting the call stack, then it's O(n) too because there will be a call for each node in the tree
"""
